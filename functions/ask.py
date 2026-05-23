from db_services.db_text import find_file
from core.ai_brain import main


def handle(file_name: str, user_ask: str):
    content = find_file(file_name)
    if content:
        full_answer = main(content, user_ask)
        return full_answer

    return "⛔ERROR⛔ Please try again with the correct file name or question."