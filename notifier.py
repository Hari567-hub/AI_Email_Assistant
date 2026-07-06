from win11toast import toast


def notify(title, message):
    toast(
        title,
        message,
        duration="short"
    )