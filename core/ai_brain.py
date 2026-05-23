import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("⛔ERROR⛔ I couldn't find your API key!")
    raise ValueError


def main(file_content, user_ask):
    genai.configure(api_key=api_key)
    system_prompt = """YOU ARE GIVEN A QUESTION AND TEXT.
ANSWER BRIEFLY.
YOUR ANSWER SHOULD BE HUMANE-FRIENDLY, SHORT, AND WITH A SMILEY EMOTICON APPROPRIATE TO THE TOPIC."""
    ai_model = "gemini-2.5-flash"
    model = genai.GenerativeModel(
        model_name=ai_model,
        system_instruction=system_prompt,
    )
    full_prompt = f"Text: {file_content}, user's ask: {user_ask}"
    print("Thinking about the answer...")

    try:
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        return f"⛔ERROR⛔ Something went wrong!\nError name: {e}"