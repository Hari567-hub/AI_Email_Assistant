from gmail.gmail_helper import get_email, mark_as_read
from gmail.email_parser import extract_body
from ai.ai_helper import summarize_email
from notification.notifier import notify
from memory.memory import is_processed, mark_processed
from memory.reminder import add_reminder

"""
Process a single unread Gmail message.

Steps:
1. Skip if already processed.
2. Extract email details.
3. Analyze using Gemini.
4. Save reminders if needed.
5. Notify the user.
6. Mark the email as read.
7. Store it in memory.
"""

def process_email(service, msg):

    if is_processed(msg["id"]):
        print("⏭️ Already processed.")
        return

    email_data = get_email(service,msg["id"] )

    payload = email_data["payload"]

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

    #log_email(sender, subject, result)

    print("=" * 60)
    print("SUMMARY      :", result.get("summary", "N/A"))
    print("CATEGORY     :", result.get("category", "N/A"))
    print("PRIORITY     :", result.get("priority", "N/A"))
    print("SCORE        :", result.get("importance_score", 0))
    print("ACTION       :", result.get("requires_action", False))
    print("REPLY        :", result.get("requires_reply", False))
    print("DEADLINE     :", result.get("deadline", "None"))

    print("NEXT STEP    :", result.get("next_action", "None"))
    if (result.get("deadline")and result.get("deadline") != "null"):

        add_reminder(subject,result["deadline"],result.get("next_action", ""))
        print("📅 Reminder saved.")

        
    print("=" * 60)

    print("Action Items:")

    for item in result.get("action_items", []):
        print(f"• {item}")

    if result.get("notify", False):

        notify(f"{subject} ({result.get('priority', 'UNKNOWN')})",result.get("summary", "No summary"))

    else:
        print("🔕 Notification skipped.")

    if result.get("category") != "Error":

        mark_as_read(service, msg["id"])
        mark_processed(msg["id"])

        print("✅ Email marked as read.")

    else:

        print("❌ AI processing failed.")