import base64
from bs4 import BeautifulSoup


def decode_data(data):
    """Decode Gmail Base64 URL-safe data."""
    if not data:
        return ""

    data += "=" * (-len(data) % 4)

    try:
        return base64.urlsafe_b64decode(data).decode(
            "utf-8",
            errors="ignore"
        )
    except Exception:
        return ""


def clean_html(html):
    """Convert HTML into readable text."""
    soup = BeautifulSoup(html, "html.parser")

    # Remove unnecessary tags
    for tag in soup(["script", "style", "head"]):
        tag.decompose()

    text = soup.get_text(separator="\n")

    # Remove blank lines
    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    return "\n".join(lines)


def search_parts(part):
    """
    Recursively search every MIME part.
    """

    html = ""
    plain = ""

    mime = part.get("mimeType")

    body = part.get("body", {})

    data = body.get("data")

    if mime == "text/html":
        html = clean_html(decode_data(data))

    elif mime == "text/plain":
        plain = decode_data(data)

    for child in part.get("parts", []):

        child_html, child_plain = search_parts(child)

        if child_html:
            html = child_html

        if child_plain:
            plain = child_plain

    return html, plain


def extract_body(payload):
    """
    Return the best email body.
    """

    html, plain = search_parts(payload)

    if html:
        return html

    return plain