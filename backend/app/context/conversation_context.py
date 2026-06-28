from app.tools.conversation import get_recent_conversation_messages


def build_conversation_context() -> str:
    messages = get_recent_conversation_messages(limit=10)

    if not messages:
        return "No recent conversation."

    conversation = []

    for message in messages:
        role = message["role"].capitalize()
        content = message["content"]

        conversation.append(
            f"{role}: {content}"
        )

    return (
        "Recent conversation:\n\n"
        + "\n".join(conversation)
    )