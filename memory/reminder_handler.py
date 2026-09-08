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

    elif " on " in command:
        parts = command.split(" on ", 1)
        date_and_task = parts[1].strip()

        date_text = date_and_task[:10]

        try:
            deadline = datetime.strptime(date_text, "%Y-%m-%d")
            keyword = " on " + date_text
        except ValueError:
            print("Please use the date format YYYY-MM-DD.")
            return

    else:
        print("I currently support today, tomorrow, or specific dates.")
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