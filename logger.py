import json
import os
from datetime import datetime

LOG_FILE = "logs.json"


def load_logs():

    if not os.path.exists(LOG_FILE):
        return []

    with open(LOG_FILE, "r") as file:
        return json.load(file)


def save_logs(logs):

    with open(LOG_FILE, "w") as file:
        json.dump(logs, file, indent=4)


def log_email(sender, subject, result):

    logs = load_logs()

    logs.append({
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sender": sender,
        "subject": subject,
        "category": result.get("category"),
        "priority": result.get("priority"),
        "summary": result.get("summary")
    })

    save_logs(logs)