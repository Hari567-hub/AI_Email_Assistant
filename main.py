import os.path
import time

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from gmail_helper import (authenticate,get_unread_emails,get_email,mark_as_read)

from email_parser import extract_body
from ai_helper import summarize_email
from config import SCOPES, MAX_EMAILS


# ------------------ Gmail Authentication ------------------

service = authenticate()


# ------------------ Read Emails ------------------

messages = get_unread_emails(service,MAX_EMAILS)

if not messages:
    print("No emails found.")
    exit()

print("\nLatest Emails\n")

for msg in messages:

    email = get_email(service,msg["id"])

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

    
    mark_as_read(service,msg["id"])

    print("✅ Email marked as read.")