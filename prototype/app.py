# Flask API (Core of the Prototype)
# this code sets up a simple Flask API to receive patient data and store it in Azure Blob Storage

from flask import Flask, request, jsonify
import os
import json
from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

app = Flask(__name__)

BLOB_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
CONTAINER_NAME = os.getenv('AZURE_CONTAINER_NAME')

blob_service_client = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
container_client = blob_service_client.get_container_client(CONTAINER_NAME)

@app.route('/ingest', methods=['POST'])
def ingest():
    data = request.json

    required_fields = ['patient_mrn', 'timestamp', 'spo2', 'heart_rate']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400
    
    patient_id = data['patient_mrn']
    timestamp = data['timestamp']

    blob_name = f'{patient_id}/{timestamp}.json'
    blob_client = container_client.go_blob_client(blob_name)

    blob_client.upload_blob(
        json.dumps(data),
        overwrite=True
    )

    return jsonify({'status':'ingested'}), 200

if __name__ == '__main__':
    app.run(debug=True)
