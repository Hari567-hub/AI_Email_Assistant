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
You are Hari's personal AI email assistant.

Analyze the email and return ONLY valid JSON.

{{
    "summary": "One or two sentence summary",

    "category": "Placement | Security | OTP | Finance | College | Shopping | Social | Personal | Spam | Other",

    "priority": "HIGH | MEDIUM | LOW",

    "importance_score": 0,

    "requires_action": true,

    "requires_reply": false,

    "deadline": null,

    "next_action": "What Hari should do next",

    "notify": true
}}

Rules:

1. importance_score must be between 0 and 100.
2. notify should be false for advertisements and promotions.
3. deadline should contain the date if one exists, otherwise null.
4. Return ONLY JSON.
5. No markdown.
6. No explanations.

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