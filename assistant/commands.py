from assistant.system import show_help, show_about
from gmail.email_monitor import check_emails_once
def execute(command):

    if command == "help":

        show_help()

        return True


    elif command == "about":

        show_about()

        return True


    elif command == "email":

        check_emails_once()

        return True


    return False