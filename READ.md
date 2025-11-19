# Event Data Pipeline mini  Project

This mini-project demonstrates the core  skills involved in building a clean, maintainable, and well-structured event-data pipeline using Python.  
It showcases practical abilities in:

- Data collection and ingestion  
- Transformation into structured domain models  
- Maintainable and modular Python code  
- Basic user-behaviour analysis and product-focused data analysis   
- Clear communication of insights  
- Engineering-ready documentation and structure  


---

## 📌 1. Project Structure


This structure mirrors common patterns used in production-oriented data engineering and internal analytics tooling.

project/
│
├── data/
│ └── raw_events.csv
│
├── src/
│ ├── data_tool.py
│ ├── models.py
│ └── init.py
│
└── README.md

---

## 📌 2. What the Tool Does

1. Loads raw event-level product data from `raw_events.csv`  
2. Validates and converts each row into a `UserEvent` **domain object** (Django-style)  
3. Performs relevant basic analytics, including:  
   - feature usage  
   - active vs inactive users  
   - churn indicators  
   - session counts  
   - platform behaviour patterns  
4. Prints a summary report suitable for technical and non-technical stakeholders

The goal is to replicate a simplified end-to-end workflow used to understand user behaviour and guide product or operational decisions.

---

## 📌 3. How to Run the Tool

Activate the virtual environment :

```bash
venv\Scripts\activate

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