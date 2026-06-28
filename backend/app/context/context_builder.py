from app.context.memory_context import build_memory_context
from app.context.todo_context import build_todo_context
from app.context.statistics_context import build_statistics_context
from app.context.habit_context import build_habit_context
from app.context.calendar_context import build_calendar_context
def build_context(plan: dict, user_message: str) -> str:
    contexts = []

    if plan["context"]["memory"]:
        memory_context = build_memory_context(user_message)
        contexts.append(memory_context)

    if plan["context"]["todos"]:
        todo_context = build_todo_context()
        contexts.append(todo_context)

    if plan["context"]["statistics"]:
        statistics_context = build_statistics_context()
        contexts.append(statistics_context)

    if plan["context"]["habits"]:
        habit_context = build_habit_context()
        contexts.append(habit_context)
        
    if plan["context"]["calendar"]:
        calendar_context = build_calendar_context()
        contexts.append(calendar_context)

    if not contexts:
        return "No additional context needed."

    return "\n\n".join(contexts)