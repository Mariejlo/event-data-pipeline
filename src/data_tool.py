"""
data_tool.py

Main tool for loading, validating, and analysing user event data.
This file ties together:
- data loading,
- domain modelling (UserEvent),
- analysis,
- and stakeholder-ready summaries.

It is structured in a modular way to demonstrate code organisation, clarity,
and readiness for productionisation.
"""

import pandas as pd
from datetime import datetime
from typing import List
from models import UserEvent


# ------------------------------------------------------------
# 1. DATA LOADING
# ------------------------------------------------------------

def load_raw_events(csv_path: str) -> pd.DataFrame:
    """
    Load the raw events CSV file into a DataFrame.

    Parameters
    ----------
    csv_path : str
        Path to the CSV file to load.

    Returns
    -------
    pd.DataFrame
        The loaded DataFrame.

    This function isolates the I/O logic, which is good practice for testing
    and maintainability.
    """
    df = pd.read_csv(csv_path)
    return df


# ------------------------------------------------------------
# 2. DATA VALIDATION & CONVERSION
# ------------------------------------------------------------

def df_to_events(df: pd.DataFrame) -> List[UserEvent]:
    """
    Convert a DataFrame of raw events into a list of UserEvent objects.

    Ensures that timestamps are parsed correctly and the domain model is respected.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing raw event data.

    Returns
    -------
    List[UserEvent]
        A list of UserEvent domain objects.
    """
    events = []

    for _, row in df.iterrows():
        event = UserEvent(
            user_id=int(row["user_id"]),
            session_id=int(row["session_id"]),
            event_timestamp=datetime.strptime(row["event_timestamp"], "%Y-%m-%d %H:%M:%S"),
            event_type=row["event_type"],
            feature_name=row["feature_name"] if pd.notna(row["feature_name"]) else None,
            plan_type=row["plan_type"],
            is_active=True if str(row["is_active"]).lower() == "true" else False
        )
        events.append(event)

    return events


# ------------------------------------------------------------
# 3. BASIC ANALYSIS
# ------------------------------------------------------------

def analyse_events(events: List[UserEvent]) -> dict:
    """
    Perform simple analytics on the event list.

    Returns a dictionary summarising:
    - number of users,
    - number of sessions,
    - most used feature,
    - churn (users with is_active=False),
    - feature usage counts.

    This simulates the kind of insights Intempus expects internally.
    """
    summary = {}

    users = set(e.user_id for e in events)
    sessions = set(e.session_id for e in events)
    features = [e.feature_name for e in events if e.feature_name]

    feature_counts = {}
    for f in features:
        feature_counts[f] = feature_counts.get(f, 0) + 1

    churned_users = set(e.user_id for e in events if not e.is_active)

    summary["total_users"] = len(users)
    summary["total_sessions"] = len(sessions)
    summary["feature_usage_counts"] = feature_counts
    summary["most_used_feature"] = max(feature_counts, key=feature_counts.get) if feature_counts else None
    summary["churned_user_ids"] = list(churned_users)

    return summary


# ------------------------------------------------------------
# 4. MAIN ENTRY POINT
# ------------------------------------------------------------

def main() -> None:
    """
    Main pipeline for the data tool.

    Steps:
    - Load raw CSV
    - Convert rows to UserEvent objects
    - Run analysis
    - Print summary

    This replicates a simple internal data tool used by product and commercial teams.
    """
    print("Loading raw events...")
    df = load_raw_events("data/raw_events.csv")

    print("Converting rows to domain objects...")
    events = df_to_events(df)

    print("Running analysis...")
    summary = analyse_events(events)

    print("\n===== SUMMARY REPORT =====\n")
    for key, value in summary.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()
