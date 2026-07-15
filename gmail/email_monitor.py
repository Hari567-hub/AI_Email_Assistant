from gmail.email_processor import process_email
from gmail.gmail_helper import authenticate, get_unread_emails
from config import MAX_EMAILS


def check_emails_once():

    print("\n📬 Checking inbox...\n")

    service = authenticate()

    unread_emails = get_unread_emails(service, MAX_EMAILS)

    if unread_emails:

        print(f"Found {len(unread_emails)} unread email(s).\n")

        for msg in unread_emails:

            process_email(service, msg)

    else:

        print("✅ No unread emails.\n")