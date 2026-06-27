from app.tools.todo import (
    add_todo,
    list_todos,
    complete_todo,
    delete_todo,
)

from app.tools.memory import (
    save_memory,
    get_memory,
    search_memory,
)

from app.tools.pomodoro import create_pomodoro

from app.tools.statistics import (
    save_completed_session,
    get_statistics,
)


TOOL_FUNCTIONS = {
    "add_todo": add_todo,
    "list_todos": list_todos,
    "complete_todo": complete_todo,
    "delete_todo": delete_todo,

    "save_memory": save_memory,
    "get_memory": get_memory,

    "create_pomodoro": create_pomodoro,

    "save_completed_session": save_completed_session,
    "get_statistics": get_statistics,
}


def run_tool(tool_name: str, arguments: dict):
    if tool_name not in TOOL_FUNCTIONS:
        return "Unknown tool"

    tool_function = TOOL_FUNCTIONS[tool_name]

    return tool_function(**arguments)