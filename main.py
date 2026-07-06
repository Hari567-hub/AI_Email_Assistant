import os.path
import time

from email_processor import process_email
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from gmail_helper import (authenticate,get_unread_emails,get_email,mark_as_read)
from config import SCOPES, MAX_EMAILS


service = authenticate()

messages = get_unread_emails(service,MAX_EMAILS)

if not messages:
    print("No emails found.")
    exit()

print("\nLatest Emails\n")

for msg in messages:
    process_email(service, msg)

    