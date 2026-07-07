from gmail_helper import get_email, mark_as_read
from email_parser import extract_body
from ai_helper import summarize_email
from notifier import notify


def process_email(service, msg):

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

    print("Summary      :", result["summary"])
    print("Priority     :", result["priority"])
    print("Category     :", result["category"])

    print("Action Items:")
    for item in result["action_items"]:
        print(f"• {item}")

    if result["priority"] == "HIGH":
        
        notify(f"🔴 {subject}",result["summary"])

    elif result["priority"] == "MEDIUM":
        print("🟡 Medium priority email.")

    else:
        print("⚪ Low priority email. Notification skipped.")

    mark_as_read(service, msg["id"])

    print("✅ Email marked as read.")