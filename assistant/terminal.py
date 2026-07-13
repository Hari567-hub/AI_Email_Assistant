from assistant.banner import show_banner
from assistant.commands import execute

def start_terminal():

    show_banner()

    print()

    print("Good Evening, Hari 👋")

    print()

    print('Type "help" to begin.')

    print()

    while True:

        command = input("> ").strip().lower()

        if command == "exit":

            print("Goodbye, Hari! 👋")

            break

        handled = execute(command)

        if handled is False:

            print(f'Unknown command: "{command}"')