import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from email_parser import extract_body
from ai_helper import summarize_email
from config import SCOPES, MAX_EMAILS


# ------------------ Gmail Authentication ------------------

creds = None

if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)

if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json",
            SCOPES
        )
        creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
        token.write(creds.to_json())

service = build("gmail", "v1", credentials=creds)


# ------------------ Read Emails ------------------

results = service.users().messages().list(
    userId="me",
    maxResults=MAX_EMAILS,
    labelIds=["INBOX"]
).execute()

messages = results.get("messages", [])

if not messages:
    print("No emails found.")
    exit()

print("\nLatest Emails\n")

for msg in messages:

    email = service.users().messages().get(
        userId="me",
        id=msg["id"]
    ).execute()

    payload = email["payload"]

    headers = payload["headers"]

    subject = "No Subject"
    sender = "Unknown"

    for header in headers:
        if header["name"] == "Subject":
            subject = header["value"]

        elif header["name"] == "From":
            sender = header["value"]

    body = extract_body(payload)

    print("-" * 60)
    print("From    :", sender)
    print("Subject :", subject)
    print()

    print("Email Preview:")
    print(body[:500])

    print("\nAI Summary:\n")

    result = summarize_email(body[:3000])

    print(result)