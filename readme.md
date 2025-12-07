# Cloud-Based Remote COPD Monitoring (Design + Optional Prototype)

This project demonstrates the design of a cloud-based healthcare system for remote monitoring of COPD patients using wearable data. The goal is to show how cloud compute, storage, databases, and serverless services can be combined to ingest physiologic data (SpO2 and heart rate), detect concerning trends, and surface meaningful alerts to patients and clinicians while controlling cost and simplfying complexity.

---

## Project Structure
```
/
├── use_case.md # One-page description of the healthcare use case
├── architecture_diagram.png
├── architecture_plan.md # Architecture diagram (Mermaid) + system design
├── reflection.md # Reflection on design choices and learning outcomes
├── README.md # Overview and instructions
└── prototype/ # Flask prototype
    ├── app.py
    ├── requirements.txt
    └── README.md
    └── video_link.text
```

## Project Overview

### Use Case
The system monitors COPD patients using consumer wearable devices that collect oxygen saturation and heart-rate data. Incoming data is stored in cloud storage, analyzed against patient-specific baselines, and used to detect early signs of deterioration. Patients receive simple awareness notifications, and clinicians receive summarized alerts through a conceptual EHR integration layer.

### Design Track
The required portion of this assignment focuses on:
- A **clear healthcare use case**
- An **Azure-based architecture** using Blob Storage, Azure SQL Database, Azure Functions, and Container Apps
- A written **data flow narrative**
- Basic **security, cost, and governance considerations**

### Prototype 
The prototype demonstrates a minimal working implementation of the ingestion portion of the system using:
- A **Flask API** (Python)
- JSON-based data ingestion via a `/ingest` endpoint
- Storage to a local SQLite database or Azure services

The prototype mirrors the ingestion portion of the full system design but does not implement EHR integration or real patient notifications.

---

## How to Read This Submission

1. Start with `use_case.md` to understand the healthcare problem.
2. Review `architecture_plan.md` with the Mermaid architecture diagram and detailed system design.
3. Read `reflection.md` for design trade-offs, and challenges.
4. Explore the `prototype/` folder to see how the Flask ingestion API would work in practice.

---

## Notes on Scope and Limitations

- All patient data used for this project is **synthetic**.
- EHR/FHIR integration is **only conceptual** and not implemented due to lack of credentials and scope constraints.
- The focus of this assignment is **architecture and cloud concepts.**

---

## Technologies Used

- **Azure Blob Storage**
- **Azure SQL Database**
- **Azure Functions (serverless)**
- **Azure Container Apps (Flask)**
- **Python / Flask**
- **Mermaid (for architecture diagram)**

---

This project demonstrates how core cloud concepts can be applied to a realistic healthcare remote monitoring scenario while remaining feasible within a student budget.