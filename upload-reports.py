import requests
import sys
import os

# Define mappings for artifact names and their scan types
SCAN_TYPES = {
    'bandit-report.json': 'Bandit Scan',
    'sca-report.json': 'Safety Scan',
    'scout-report.sarif': 'Scout Scan'
}

ARTIFACTS_DIR = sys.argv[1]

headers = {
    'Authorization': 'Token 548afd6fab3bea9794a41b31da0e9404f733e222'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

# Iterate over each artifact file
for file_name, scan_type in SCAN_TYPES.items():
    file_path = os.path.join(ARTIFACTS_DIR, file_name)
    
    if not os.path.exists(file_path):
        print(f"{file_name} not found. Skipping upload.")
        continue

    print(f"Uploading {file_name} as {scan_type}...")
    
    data = {
        'active': True,
        'verified': True,
        'scan_type': scan_type,
        'minimum_severity': 'Low',
        'engagement': 6
    }

    files = {
        'file': open(file_path, 'rb')
    }

    response = requests.post(url, headers=headers, data=data, files=files)

    if response.status_code == 201:
        print(f"Successfully uploaded {file_name}")
    else:
        print(f"Failed to upload {file_name}: {response.content}")
