from assistant.system import show_help, show_about
from gmail.email_monitor import check_emails_once
from core.router import route_command
from memory.reminder import show_reminders
from memory.reminder_handler import create_reminder
import os


def execute(command):

    intent = route_command(command)

    if intent == "EMAIL_CHECK":
        check_emails_once()
        return True

    elif intent == "HELP":
        show_help()
        return True

    elif intent == "ABOUT":
        show_about()
        return True

    elif intent == "CLEAR":
        os.system("cls")
        return True

    elif intent == "EXIT":
        return True

    elif intent == "CREATE_REMINDER":
        create_reminder(command)
        return True

    elif intent == "REMINDER_LIST":
        show_reminders()
        return True


    return False