def create_plan(user_message: str):
    message = user_message.lower()

    plan = {
        "context": {
            "memory": False,
            "todos": False,
            "statistics": False,
            "calendar": False,
            "habits": False,
        },

        "allowed_tools": [],

        "reasons": []
    }

    # --------------------
    # Todo
    # --------------------

    if any(word in message for word in [
        "todo",
        "task",
        "work",
        "today",
        "priority",
        "finish"
    ]):

        plan["context"]["todos"] = True

        plan["allowed_tools"] += [
            "add_todo",
            "list_todos",
            "complete_todo",
            "delete_todo"
        ]

        plan["reasons"].append("Todo management")

    # --------------------
    # Memory
    # --------------------

    if any(word in message for word in [
        "remember",
        "goal",
        "routine",
        "preference",
        "wake up",
        "name"
    ]):

        plan["context"]["memory"] = True

        plan["allowed_tools"] += [
            "save_memory",
            "get_memory"
        ]

        plan["reasons"].append("Memory lookup")

    # --------------------
    # Pomodoro
    # --------------------

    if any(word in message for word in [
        "pomodoro",
        "focus",
        "study"
    ]):

        plan["allowed_tools"].append("create_pomodoro")
        plan["reasons"].append("Focus planning")

    # --------------------
    # Statistics
    # --------------------

    if any(word in message for word in [
        "statistics",
        "progress",
        "completed"
    ]):

        plan["context"]["statistics"] = True

        plan["allowed_tools"] += ["get_statistics","save_completed_session"]

        plan["reasons"].append("Statistics lookup")

    # --------------------
    # Habits
    # --------------------

    if any(word in message for word in [
        "habit",
        "track",
        "streak",
        "daily",
        "routine"
    ]):
        plan["context"]["habits"] = True
        plan["allowed_tools"] += [
        "add_habit",
        "list_habits",
        "complete_habit"
        ]

        plan["reasons"].append("Habit tracking")

    return plan