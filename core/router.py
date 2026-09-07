def route_command(command):

    command = command.lower().strip()

    if command in ["email", "emails", "inbox"]:
        return "EMAIL_CHECK"

    elif any(word in command for word in ["check", "show", "read"]):
        if any(word in command for word in ["email", "emails", "mail", "inbox"]):
            return "EMAIL_CHECK"

    elif command in ["help", "?"]:
        return "HELP"

    elif command == "about":
        return "ABOUT"

    elif command == "clear":
        return "CLEAR"

    elif command in ["exit", "quit"]:
        return "EXIT"

    return "UNKNOWN"