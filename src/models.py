"""
models.py

Domain models for user events in a time registration product.
Structured in a Django-style way so it can later be mapped to a real database table.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class UserEvent:
    """
    Represents a single user event in the product.

    Fields here mirror what we would typically store in a database row
    or Django ORM model.
    """
    user_id: int
    session_id: int
    event_timestamp: datetime
    event_type: str          #  "login", "feature_use", "error"
    feature_name: Optional[str]  # which feature was used (if any)
    plan_type: str           # "basic", "pro", "trial"
    is_active: bool           # whether the user is currently active
