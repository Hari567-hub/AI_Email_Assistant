from datetime import datetime, timedelta
from memory.reminder import add_reminder


def create_reminder(command):

    command = command.lower().strip()

    if "tomorrow" not in command:
        print("I currently support reminders for tomorrow.")
        return

    task = command.split("tomorrow", 1)[1].strip()

    if task.startswith("to "):
        task = task[3:]

    deadline = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")

    add_reminder(
        "Manual Reminder",
        deadline,
        task
    )

    print("📅 Reminder created.")
    print("Task     :", task)
    print("Deadline :", deadline)