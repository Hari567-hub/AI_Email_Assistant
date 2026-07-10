"""
Desktop notification utilities.

This module displays Windows notifications
for important emails.
"""
from win11toast import toast


def notify(title, message):
    """
    Display a Windows desktop notification.

    Args:
        title (str): Notification title.
        message (str): Notification body.
    """

    try:
        toast(
            title,
            message,
            duration="short"
        )

    except Exception as e:
        print(f"Notification Error: {e}")