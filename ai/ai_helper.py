import json
import os
from config import GEMINI_MODEL
from dotenv import load_dotenv
from google import genai
from ai.prompts import EMAIL_ANALYSIS_PROMPT

load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")

)


def summarize_email(email_text):
    """
    Analyze an email using Gemini AI.

    Args:
        email_text (str): Extracted email body.

    Returns:
        dict: Structured AI analysis of the email.
    """

    prompt = EMAIL_ANALYSIS_PROMPT.format(email_text=email_text)

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
)
        
        return json.loads(response.text)

    except json.JSONDecodeError:
        return {
            "summary": "Failed to process email.",
            "category": "Error",
            "priority": "LOW",
            "importance_score": 0,
            "requires_action": False,
            "requires_reply": False,
            "deadline": None,
            "next_action": "Retry processing later.",
            "notify": False,
            "action_items": []
        }

    except Exception as e:
        return {
            "summary": str(e),
            "category": "Error",
            "priority": "LOW",
            "importance_score": 0,
            "requires_action": False,
            "requires_reply": False,
            "deadline": None,
            "next_action": "Retry processing later.",
            "notify": False,
            "action_items": []
        }