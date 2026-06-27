from app.tools.memory import search_memory


def build_memory_context(user_message: str) -> str:
    relevant_memories = search_memory(user_message)

    if not relevant_memories:
        return "No relevant saved memory found."

    return f"""
    Relevant user memory:
    {relevant_memories}
    """