from fastapi import FastAPI
from fastapi.responses import Response
import requests
from msal import PublicClientApplication
import json

app = FastAPI()

# --- Replace these with your values ---
TENANT_ID = "da157993-5112-44a5-97ab-b0674b677758"
CLIENT_ID = "1ead5cee-6926-41b3-8364-b9d671727a12"
D365_URL = "https://org932fcf4e.crm6.dynamics.com/api/data/v9.2/accounts?$top=5"

SCOPE = [f"https://org932fcf4e.crm6.dynamics.com/.default"]

msal_app = PublicClientApplication(
    client_id=CLIENT_ID,
    authority=f"https://login.microsoftonline.com/{TENANT_ID}"
)

def get_access_token():
    accounts = msal_app.get_accounts()
    if accounts:
        result = msal_app.acquire_token_silent(SCOPE, account=accounts[0])
        if result and "access_token" in result:
            return result["access_token"]

    result = msal_app.acquire_token_interactive(scopes=SCOPE)
    if "access_token" not in result:
        raise ValueError(f"Could not obtain access token: {result}")
    return result['access_token']

@app.get("/")
def read_accounts():
    try:
        token = get_access_token()
    except Exception as e:
        return Response(
            content=json.dumps({"error": "Failed to get access token", "details": str(e)}, indent=4),
            media_type="application/json",
            status_code=500
        )

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json"
    }

    response = requests.get(D365_URL, headers=headers)

    if response.status_code == 200:
        data = response.json()
        accounts = [
            {
                "name": a.get("name", "N/A"),
                "main_phone": a.get("telephone1", "N/A"),
                "city": a.get("address1_city", "N/A")
            }
            for a in data.get("value", [])
        ]
        # Convert to pretty JSON string
        return Response(
            content=json.dumps({"accounts": accounts}, indent=4),
            media_type="application/json"
        )
    else:
        return Response(
            content=json.dumps({
                "error": "Failed to fetch data",
                "status_code": response.status_code,
                "details": response.text
            }, indent=4),
            media_type="application/json",
            status_code=response.status_code
        )

@app.get("/health")
def health_check():
    return Response(
        content=json.dumps({"status": "ok"}, indent=4),
        media_type="application/json"
    )
