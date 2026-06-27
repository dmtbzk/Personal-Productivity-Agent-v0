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

from app.tools.habits import (
    add_habit,
    list_habits,
    complete_habit,
)

import json

TOOL_FUNCTIONS = {
    "add_todo": add_todo,
    "list_todos": list_todos,
    "complete_todo": complete_todo,
    "delete_todo": delete_todo,

    "save_memory": save_memory,
    "get_memory": get_memory,
    "search_memory": search_memory,

    "create_pomodoro": create_pomodoro,

    "save_completed_session": save_completed_session,
    "get_statistics": get_statistics,

    "add_habit": add_habit,
    "list_habits": list_habits,
    "complete_habit": complete_habit,
}


def run_tool(tool_name: str, arguments: dict):
    if tool_name not in TOOL_FUNCTIONS:
        return "Unknown tool"

    tool_function = TOOL_FUNCTIONS[tool_name]

    return tool_function(**arguments)

def execute_tool_calls(response):
    tool_outputs = []

    for item in response.output:
        if item.type == "function_call":
            tool_name = item.name
            call_id = item.call_id
            arguments = json.loads(item.arguments)

            print("Tool selected:", tool_name)
            print("Tool arguments:", arguments)

            tool_result = run_tool(tool_name, arguments)

            print("Tool result:", tool_result)

            tool_outputs.append({
                "type": "function_call_output",
                "call_id": call_id,
                "output": str(tool_result)
            })

    return tool_outputs