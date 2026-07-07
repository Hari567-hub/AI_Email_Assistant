import json
import os
from config import GEMINI_MODEL
from dotenv import load_dotenv
from google import genai

load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def summarize_email(email_text):
    prompt = f"""
You are an AI Email Assistant.

Analyze the email and respond ONLY with valid JSON.

Return exactly this format:

{{
    "summary": "...",
    "priority": "HIGH | MEDIUM | LOW",
    "category": "...",
    "action_items": [
        "...",
        "..."
    ]
}}

Rules:
- Return ONLY JSON.
- Do not use markdown.
- Do not use triple backticks.
- Do not explain anything outside the JSON.

Email:
{email_text}
"""

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
)
        
        return json.loads(response.text)

    except json.JSONDecodeError:
        return {
            "summary": "Failed to parse Gemini response.",
            "priority": "LOW",
            "category": "Unknown",
            "action_items": []
        }

    except Exception as e:
        return {
            "summary": str(e),
            "priority": "LOW",
            "category": "Error",
            "action_items": []
    }