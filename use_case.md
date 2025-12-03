# Use Case: Remote COPD Exacerbation Monitoring via Wearables and Azure Cloud

## Clinical Problem
Chronic Obstructive Pulmonary Disease(COPD) exacerbations are a major driver of emergency visits and hospitalizations. Between 30%-50% of people with COPD experience at least one exacerbation per year, and this risk increases with disease severity and previous exacerbations. Many patients deteriorate for several days before they seek care. During that period, subtle changes in oxygen saturation (SpO2) and heart rate(HR) can signal early decompensation, but clinicians and patients rarely see those trends in real time. 

The problem this system addresses is the lack of early, actionable visibility into physiological trends for COPD patients living at home. Patients are often unaware that their physiological status is worsening until symptoms become severe. Clinicians are either not aware of worsening trends are suffering from overwhelming data fatigue. 

The proposed solution is a cloud-based remote patient monitoring mini-pipeline that continuously ingests SpO2 and heart-rate data from consumer wearables, compares trends against individualized baselines, and communicates meaningful feedback to both clinicians and patients. Clinicians receive summarized alerts only when thresholds are crossed, while patients receive simple, non-alarming notifications that their readings suggest early decline and that follow-up actions may be needed. The goal is to prevent avoidable COPD hospitalizations through earlier awareness and intervention while minimizing alert fatigue.

The primary users include COPD patients enrolled in remote monitoring programs, pulmonologists and primary-care clinicians, and care managers/nurses responsible for triaging alerts.


## Data Sources
* Wearable sensor data:

Continuous SpO2 and heart-rate measurements collected from consumer wearable devices like Apple Watch. Data is received as JSON payloads via a vendor API at regular intervals every 5-30 minutes. 

* Patient baseline and configuration data:

Patient-specific SpO2 baselines, resting heart-rate profiles, and alert thresholds stored in a managed Azure database to support individualized monitoring.

* Alert and event data:

Records of detected trend abnormalities, severity classification, notification status, and resolution notes, stored for auditing and analytics.

* EHR integration data:

Summarized trends and alerts are sent to the patient via a mobile notification or dashboard, and to clinicians via FHIR-based integration with the EHR like EPIC. 

## Basic Workflow
1. Wearable devices continuously collect SpO2 and heart rate readings from COPD patients at home.
2. The wearable vendor's API sends JSON data to a secure Azure ingestion endpoint.
3. Incoming data is stored in an Azure Blob Storage as raw sensor data.
4. An Azure Function retrieves the patient's baselines values from a managed database and evaluates recent trends against personalized thresholds.
5. If there is no concerning trends, data is stored without alerting.
6. If thresholds are exceeded, the patient receives a simple notification to prompt awareness and self-management actions.
7. Clinicians and care managers/nurses receive summarized alerts in EHR only when trends indicate clinical significance.
8. Follow-up actions are documented and stored for ongoing monitoring and system improvement.