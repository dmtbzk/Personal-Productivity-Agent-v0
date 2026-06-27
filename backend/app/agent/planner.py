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

        "reason": ""
    }

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

        plan["reason"] = "Todo management"

    if any(word in message for word in [
        "remember",
        "my",
        "me",
        "goal",
        "routine",
        "preference"
    ]):
        plan["context"]["memory"] = True

        plan["allowed_tools"] += [
            "save_memory",
            "get_memory"
        ]

        plan["reason"] = "Memory lookup"

    if any(word in message for word in [
        "pomodoro",
        "focus",
        "study"
    ]):
        plan["allowed_tools"].append("create_pomodoro")

    if any(word in message for word in [
        "statistics",
        "progress",
        "completed"
    ]):
        plan["context"]["statistics"] = True

        plan["allowed_tools"] += [
            "get_statistics"
        ]

    return plan