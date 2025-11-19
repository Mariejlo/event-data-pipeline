# Event Data Pipeline mini  Project
This project is a compact example of how I structure data ingestion, transformation, and user-behaviour analysis in Python. The goal was to create a simple, maintainable, and extensible pipeline that reflects how internal data tools are designed in modern engineering teams.

Although small in size, the project follows the same principles I apply in larger systems: clear modelling, separation of responsibilities, predictable folder structure, and documentation that makes collaboration easier for others.
---


## 1. Project Overview

The repository contains a minimal pipeline that:

- ingests raw product event data

- validates and transforms it into structured domain objects

- produces a small set of behavioural insights

- keeps the codebase clean, modular, and ready to extend

This is the type of foundation typically used when building internal analytics tools, behaviour-tracking components, or data collection services that need to grow over time.

---

## 2. Project Structure


This structure mirrors common patterns used in production-oriented data engineering and internal analytics tooling.

event-data-pipeline/
│
├── data/
│   └── raw_events.csv
│
├── src/
│   ├── models.py          # Domain model (UserEvent)
│   ├── ingestion.py       # Ingestion + CSV loading
│   ├── analysis.py        # Behaviour analysis functions
│   └── data_tool.py       # Entry point script
│
├── .gitignore
└── README.md

The structure mirrors a typical internal tool layout:

- models.py holds domain objects

- ingestion.py handles data loading

- analysis.py contains business logic

- data_tool.py serves as the execution layer

Keeping these areas separate makes the code easier to test, update, and maintain.

---

## 3. How the Pipeline works

Step 1: Load raw event data

A simple CSV (placeholder data) is used to simulate product event logs.


Step 2: Convert each row into a domain model

The UserEvent dataclass provides a clean, Django-style representation of each event.


Step 3: Run behavioural analysis

The analysis module outputs:

- user activity patterns

- feature usage

- basic churn indicators

- sign-in frequencies

- platform preferences

Step 4: Print a readable summary

The script generates a concise terminal report suitable for a product manager, backend lead, or commercial stakeholder.

The goal is to replicate a simplified end-to-end workflow used to understand user behaviour and guide product or operational decisions.

---

## 4. How to Run the project

Activate the virtual environment :

```bash
venv\Scripts\activate
´´´
Run the script:
python src/data_tool.py

Then, you will see a summary printed in the terminal.

---

## 📌 4. Domain Modelling Approach

The UserEvent class in models.py is implemented using Python dataclasses, mirroring Django ORM conventions:

    A. Strong typing

    B. Clear definition of each field

    C. Separation of domain logic from I/O logic

This separation is intentional so the project could be extended into  more complex pipeline in the future or integrate with frameworks such as Django ORM, SQLAlchemy, or Pydantic.


--- 

## 📌 5. Engineering Notes (for Backend Team Lead / CTO)
🔹 Design Decisions

Modular Python structure to allow independent testing of ingestion, validation, and analysis.

Domain modelling first, reflecting how Intempus stores product event data.

Separation of concerns:

load_raw_events() handles I/O

df_to_events() handles validation & transformation

analyse_events() handles business logic

🔹 Scalability Considerations

The ingestion pipeline can easily be extended to read from APIs or message queues.

The UserEvent model can map directly to Django models or Pydantic schemas.

Analysis functions can be moved into a dedicated /analysis module for future expansion.

🔹 Future Enhancements


Add automated tests (pytest)

Add charts or reporting

Build a CLI wrapper

Introduce data validation frameworks

Containerise with Docker

Add scheduling/orchestration (Airflow, Prefect, Dagster)


---

📌 6. Summary


This project presents:

Clean, production-minded Python code

A maintainable structure suitable for collaboration

An event-driven data model with typed domain objects

Practical behavioural analytics

Documentation that supports both engineering and product teams

It serves as a compact demonstration of data engineering fundamentals as well as the ability to design and communicate a real-world data workflow.
