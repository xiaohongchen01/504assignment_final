# this code generates synthetic data for testing purposes

import requests
import random
from datetime import datetime
import time


BASE_URL = 'https://copd-rpm-api-hfc8bccmfggwbgf8.eastus-01.azurewebsites.net/ingest'

PATIENT_ID = "COPD_001"

while True:
    payload = {
        "patient_mrn": PATIENT_ID,
        "timestamp": datetime.utcnow().isoformat(),
        "spo2": random.randint(85,100),
        "heart_rate": random.randint(70, 120)
    }

    response = requests.post(BASE_URL, json=payload)

    print("Status:", response.status_code)
    try:
        print("JSON Response:", response.json())
    except ValueError:
        print("Response:", response.text[:200])

    time.sleep(10)

    # can later change BASE_URL 