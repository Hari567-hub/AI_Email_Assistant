import json
import os
from datetime import datetime

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

    for reminder in reminders:
        if (
            reminder["subject"] == subject
            and reminder["deadline"] == deadline
        ):
            return

    reminders.append({
        "subject": subject,
        "deadline": deadline,
        "action": action
    })

    save_reminders(reminders)

def show_reminders():

        reminders = load_reminders()

        if not reminders:
            print("📅 No pending reminders.\n")
            return

        print("\n📅 Pending Reminders")
        print("=" * 50)

        for reminder in reminders:

            print(f"Subject  : {reminder['subject']}")
            print(f"Deadline : {reminder['deadline']}")
            print(f"Action   : {reminder['action']}")
            print("-" * 50)

        print()   

def remove_expired_reminders():

        reminders = load_reminders()

        today = datetime.today().date()

        valid_reminders = []

        for reminder in reminders:

            try:
                deadline = datetime.strptime(
                    reminder["deadline"],
                    "%Y-%m-%d"
                ).date()

                if deadline >= today:
                    valid_reminders.append(reminder)

            except:
                valid_reminders.append(reminder)

        save_reminders(valid_reminders)