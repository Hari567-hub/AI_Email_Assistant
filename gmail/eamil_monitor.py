"""
Main entry point for the AI Email Assistant.

Initializes Gmail, loads reminders,
and continuously monitors unread emails.
"""
import time

from gmail.email_processor import process_email
from gmail.gmail_helper import (authenticate,get_unread_emails)
from config import MAX_EMAILS, CHECK_INTERVAL
from memory.reminder import (show_reminders,remove_expired_reminders)

print("=" * 60)
print("🤖 AI Email Assistant Started")
print("=" * 60)

service = authenticate()
print("✅ Gmail Connected")

remove_expired_reminders()
show_reminders()

try:
    while True:

        unread_emails = get_unread_emails(service, MAX_EMAILS)

        if unread_emails:

            print("\nChecking for new emails...\n")

            for msg in unread_emails:
                process_email(service, msg)

        else:
            print("No new emails.")

        print(f"\nWaiting {CHECK_INTERVAL} seconds...\n")
        time.sleep(CHECK_INTERVAL)

except KeyboardInterrupt:
    print("\n🛑 AI Email Agent stopped.")