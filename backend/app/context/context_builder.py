from app.context.memory_context import build_memory_context
from app.context.todo_context import build_todo_context


def build_context(user_message: str) -> str:
    contexts = []

    memory_context = build_memory_context(user_message)
    todo_context = build_todo_context()

    if memory_context:
        contexts.append(memory_context)

    if todo_context:
        contexts.append(todo_context)

    return "\n\n".join(contexts)