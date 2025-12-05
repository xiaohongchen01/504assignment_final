# this code generates synthetic data for testing purposes

import requests
import random
from datatime import datetime
import time


BASE_URL = 'http://127.0.0.1:5000/ingest'

PATIENT_ID = "COPD_001"

while True:
    payload = {
        "patient_mrn": PATIENT_ID,
        "timestamp": datetime.utcnow().isoformat(),
        "spo2": random.randint(85,100),
        "heart_rate": random.randint(70, 120)
    }

    response = requests.post(BASE_URL, json=payload)
    print(response.status_code, response.json())

    time.sleep(10)

    # can later change BASE_URL 