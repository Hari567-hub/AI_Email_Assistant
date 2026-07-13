from assistant.system import show_help, show_about
def execute(command):

    if command == "help":

        show_help()

        return True


    elif command == "about":

        show_about()

        return True


    elif command == "email":

        print("\n📧 Starting Email Monitor...")

        return True


    return False