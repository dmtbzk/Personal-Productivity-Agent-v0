from app.tools.conversation import save_conversation_message


def save_user_message(content: str):
    save_conversation_message("user", content)


def save_assistant_message(content: str):
    save_conversation_message("assistant", content)