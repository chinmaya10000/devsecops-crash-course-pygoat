import requests
import sys
import os

file_name = sys.argv[1]
scan_type = ''

if file_name == 'bandit-report.json':
    scan_type = 'Bandit Scan'
elif file_name == 'sca-report.json':
    scan_type = 'Safety Scan'
elif file_name == 'scout-report.sarif':
    scan_type = 'Scout Scan'

# Check if file exists before uploading
if not os.path.exists(file_name):
    print(f"{file_name} not found. Skipping upload.")
    sys.exit(0)

headers = {
    'Authorization': 'Token 548afd6fab3bea9794a41b31da0e9404f733e222'
}

url = 'https://demo.defectdojo.org/api/v2/import-scan/'

data = {
    'active': True,
    'verified': True,
    'scan_type': scan_type,
    'minimum_severity': 'Low',
    'engagement': 6
}

files = {
    'file': open(file_name, 'rb')
}

response = requests.post(url, headers=headers, data=data, files=files)

if response.status_code == 201:
    print('Scan results imported successfully')
else:
    print(f'Failed to import scan results: {response.content}')
