import json
import os

REMINDER_FILE = "reminders.json"


def load_reminders():

    if not os.path.exists(REMINDER_FILE):
        return []

    with open(REMINDER_FILE, "r") as file:
        return json.load(file)


def save_reminders(reminders):

    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file, indent=4)


def add_reminder(subject, deadline, action):

    reminders = load_reminders()

    reminders.append({
        "subject": subject,
        "deadline": deadline,
        "action": action
    })

    save_reminders(reminders)