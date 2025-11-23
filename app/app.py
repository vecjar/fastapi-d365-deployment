from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from msal import ConfidentialClientApplication
import requests
import os

app = FastAPI()

# Azure AD App Registration values
CLIENT_ID = "1ead5cee-6926-41b3-8364-b9d671727a12"
CLIENT_SECRET = "fjZ8Q~qENY5qaKgEu3NhQYHKjcNmEPUWU7lmCcBQ"
TENANT_ID = "da157993-5112-44a5-97ab-b0674b677758" 
REDIRECT_URI = "https://fastapiproject-webapp.azurewebsites.net/getAToken" 
SCOPE = ["https://org932fcf4e.crm6.dynamics.com/user_impersonation"]

# MSAL ConfidentialClientApplication for web app login
msal_app = ConfidentialClientApplication(
    client_id=CLIENT_ID,
    client_credential=CLIENT_SECRET,
    authority=f"https://login.microsoftonline.com/{TENANT_ID}"
)

# In-memory token cache
token_cache = {}

@app.get("/")
def login():
    """Redirect user to Microsoft login page"""
    auth_url = msal_app.get_authorization_request_url(
        SCOPE,
        redirect_uri=REDIRECT_URI
    )
    return RedirectResponse(auth_url)

@app.get("/getAToken")
def receive_token(request: Request):
    """Receive auth code and exchange for access token"""
    code = request.query_params.get("code")
    if not code:
        return HTMLResponse("<h2>Error: no auth code returned.</h2>")

    result = msal_app.acquire_token_by_authorization_code(
        code,
        scopes=SCOPE,
        redirect_uri=REDIRECT_URI
    )

    if "access_token" not in result:
        return HTMLResponse(f"<h2>Failed to get token</h2><pre>{result}</pre>")

    access_token = result["access_token"]
    token_cache["access_token"] = access_token  # store for demo

    # Fetch top 5 accounts from Dataverse
    D365_URL = "https://org932fcf4e.crm6.dynamics.com/api/data/v9.2/accounts?$top=5"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }
    response = requests.get(D365_URL, headers=headers)

    if response.status_code == 200:
        accounts = response.json().get("value", [])
        html = "<h2>Top 5 Accounts</h2><ul>"
        for a in accounts:
            html += f"<li>{a.get('name', 'N/A')} - {a.get('telephone1', 'N/A')} - {a.get('address1_city', 'N/A')}</li>"
        html += "</ul>"
        return HTMLResponse(html)
    else:
        return HTMLResponse(f"<h2>Failed to fetch data</h2><pre>{response.text}</pre>")

@app.get("/health")
def health_check():
    return {"status": "ok"}
