from gmail_helper import get_email, mark_as_read
from email_parser import extract_body
from ai_helper import summarize_email
from notifier import notify
from memory import is_processed, mark_processed
from reminder import add_reminder

def process_email(service, msg):

    if is_processed(msg["id"]):
        print("⏭️ Already processed.")
        return

    email = get_email(service,msg["id"] )

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

    print("=" * 60)
    print("SUMMARY      :", result.get("summary", "N/A"))
    print("CATEGORY     :", result.get("category", "N/A"))
    print("PRIORITY     :", result.get("priority", "N/A"))
    print("SCORE        :", result.get("importance_score", 0))
    print("ACTION       :", result.get("requires_action", False))
    print("REPLY        :", result.get("requires_reply", False))
    print("DEADLINE     :", result.get("deadline", "None"))
    if result.get("deadline"):

        add_reminder(subject,result["deadline"],result.get("next_action", ""))

    print("📅 Reminder Saved")
    print("NEXT STEP    :", result.get("next_action", "None"))
    if (
        result.get("deadline")
        and result.get("deadline") != "null"
    ):

        add_reminder(
            subject,
            result["deadline"],
            result.get("next_action", "")
        )

        print("📅 Reminder Saved")
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