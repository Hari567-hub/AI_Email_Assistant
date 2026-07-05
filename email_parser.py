import base64
from bs4 import BeautifulSoup


def decode_data(data):
    """Decode Gmail Base64 URL-safe data."""
    return base64.urlsafe_b64decode(data + "=" * (-len(data) % 4)).decode(
        "utf-8", errors="ignore"
    )


def clean_html(html):
    """Convert HTML into readable plain text."""
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text(separator="\n", strip=True)


def extract_body(payload):
    """
    Extract email body.
    Preference:
        1. HTML
        2. Plain text
    """

    html_body = None
    plain_body = None

    parts = payload.get("parts", [])

    for part in parts:
        mime = part.get("mimeType")

        if mime == "text/html":
            data = part.get("body", {}).get("data")
            if data:
                html_body = clean_html(decode_data(data))

        elif mime == "text/plain":
            data = part.get("body", {}).get("data")
            if data:
                plain_body = decode_data(data)

    if html_body:
        return html_body

    if plain_body:
        return plain_body

    return ""