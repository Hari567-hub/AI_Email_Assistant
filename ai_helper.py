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

Analyze the following email and return:

Summary:
Priority:
Action Items:

Email:
{email_text}
"""

    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
)
        
        return response.text

    except Exception as e:
        return f"Gemini Error:\n{e}"