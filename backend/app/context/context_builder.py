from app.agent.planner import create_plan
from app.context.memory_context import build_memory_context
from app.context.todo_context import build_todo_context


def build_context(user_message: str) -> str:
    plan = create_plan(user_message)

    contexts = []

    if plan["context"]["memory"]:
        memory_context = build_memory_context(user_message)
        contexts.append(memory_context)

    if plan["context"]["todos"]:
        todo_context = build_todo_context()
        contexts.append(todo_context)

    if not contexts:
        return "No additional context needed."

    return "\n\n".join(contexts)