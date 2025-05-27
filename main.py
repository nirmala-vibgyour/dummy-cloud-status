import os
import requests
import urllib3
from dotenv import load_dotenv

# Suppress SSL warnings for self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Load .env file
load_dotenv()

# Environment variables
controller_ip = os.getenv("AVI_CONTROLLER_IP")
cloud_uuid = os.getenv("CLOUD_UUID")
sessionid = os.getenv("SESSIONID")
csrftoken = os.getenv("CSRFTOKEN")
avi_version = os.getenv("X_AVI_VERSION")
avi_tenant = os.getenv("AVI_TENANT")

# API URL
url = f"https://{controller_ip}/api/cloud/{cloud_uuid}/status/"

# Headers
headers = {
    "Content-Type": "application/json",
    "X-CSRFToken": csrftoken,
    "X-Avi-Version": avi_version,
    "X-Avi-Tenant": avi_tenant,
    "Referer": f"https://{controller_ip}/",
    "Cookie": f"sessionid={sessionid}; csrftoken={csrftoken}"
}

# Request cloud status
try:
    response = requests.get(url, headers=headers, verify=False)
    response.raise_for_status()
    data = response.json()

    # Output
    print(f"Cloud status: {data.get('state')}")
    if 'reason' in data:
        print(f"Reason: {data['reason']}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
