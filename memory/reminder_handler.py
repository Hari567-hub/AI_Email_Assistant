from datetime import datetime, timedelta
from memory.reminder import add_reminder


def create_reminder(command):

    command = command.lower().strip()

    if "tomorrow" in command:
        deadline = datetime.today() + timedelta(days=1)
        keyword = "tomorrow"

    elif "today" in command:
        deadline = datetime.today()
        keyword = "today"

    else:
        print("I currently support reminders for today or tomorrow.")
        return

    task = command.split(keyword, 1)[1].strip()

    if task.startswith("to "):
        task = task[3:]

    deadline = deadline.strftime("%Y-%m-%d")

    add_reminder(
        "Manual Reminder",
        deadline,
        task
    )

    print("📅 Reminder created.")
    print("Task     :", task)
    print("Deadline :", deadline)