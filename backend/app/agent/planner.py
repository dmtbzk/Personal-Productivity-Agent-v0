def plan_context_needs(user_message: str):
    message = user_message.lower()

    needs = {
        "memory": False,
        "todos": False,
        "statistics": False,
        "calendar": False,
        "habits": False
    }

    if any(word in message for word in ["me", "my", "myself", "routine", "goal", "prefer", "remember"]):
        needs["memory"] = True

    if any(word in message for word in ["todo", "task", "work on", "today", "priority", "finish"]):
        needs["todos"] = True

    if any(word in message for word in ["progress", "stats", "statistics", "completed", "how many"]):
        needs["statistics"] = True

    if any(word in message for word in ["calendar", "meeting", "schedule", "appointment"]):
        needs["calendar"] = True

    if any(word in message for word in ["habit", "streak", "routine"]):
        needs["habits"] = True

    return needs