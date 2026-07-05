from __future__ import print_function
from ai_helper import summarize_email
import base64
from email import message_from_bytes
import os.path
import base64
from bs4 import BeautifulSoup

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Read-only access to Gmail
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

creds = None

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
        token.write(creds.to_json())

service = build("gmail", "v1", credentials=creds)

results = service.users().messages().list(
    userId="me",
    maxResults=1,
    labelIds=["INBOX"]
).execute()

messages = results.get("messages", [])

if not messages:
    print("No messages found.")
else:
    print("Latest Emails:")
    for msg in messages:
        email = service.users().messages().get(
            userId="me",
            id=msg["id"]
        ).execute()

        headers = email["payload"]["headers"]

        subject = "No Subject"
        sender = "Unknown"

        for header in headers:
            if header["name"] == "Subject":
                subject = header["value"]
            elif header["name"] == "From":
                sender = header["value"]

        print("-" * 50)
        print("From :", sender)
        print("Subject :", subject)
body = ""

payload = email.get("payload", {})
import json

print(json.dumps(payload, indent=2))
def extract_body(parts):
    for part in parts:
        mime = part.get("mimeType")

        if mime == "text/plain":
            data = part["body"].get("data")
            if data:
                return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")

        elif mime == "text/html":
            data = part["body"].get("data")
            if data:
                html = base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")
                soup = BeautifulSoup(html, "html.parser")
                return soup.get_text(separator="\n")

        elif "parts" in part:
            result = extract_body(part["parts"])
            if result:
                return result

    return ""

if "parts" in payload:
    body = extract_body(payload["parts"])
    print("=" * 60)
    print("BODY LENGTH:", len(body))
    print("=" * 60)
    print(body[:500])
    print("=" * 60)
else:
    data = payload.get("body", {}).get("data")
    
    if data:
        body = base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")

        print("\nEmail Body:\n")
        print("\nAnalyzing with Gemini...\n")

        result = summarize_email(body[:3000])

        print(result)      # Print only the first 1000 characters
        print("-" * 50)