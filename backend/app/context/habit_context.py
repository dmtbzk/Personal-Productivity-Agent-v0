from app.tools.habits import list_habits


def build_habit_context() -> str:
    habits = list_habits()

    if not habits:
        return "No habits found."

    return f"""
Tracked habits:
{habits}
"""