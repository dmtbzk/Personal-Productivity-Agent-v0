from openai import OpenAI
from dotenv import load_dotenv
import json

from app.tool_registry import TOOLS

from app.tools.todo import add_todo, list_todos, complete_todo
from app.tools.memory import save_memory, get_memory
from app.tools.pomodoro import create_pomodoro
from app.tools.statistics import save_completed_session, get_statistics

load_dotenv()

client = OpenAI()


def run_agent(user_message: str) -> str:
    response = client.responses.create(
        model="gpt-4o-mini",
        input=user_message,
        tools=TOOLS
    )

    tool_outputs = []

    for item in response.output:
        if item.type == "function_call":
            tool_name = item.name
            call_id = item.call_id
            arguments = json.loads(item.arguments)

            print("Tool selected:", tool_name)
            print("Tool arguments:", arguments)

            if tool_name == "add_todo":
                tool_result = add_todo(arguments["task"])

            elif tool_name == "list_todos":
                tool_result = str(list_todos())

            elif tool_name == "complete_todo":
                tool_result = complete_todo(arguments["index"])

            elif tool_name == "save_memory":
                tool_result = save_memory(arguments["note"])

            elif tool_name == "get_memory":
                tool_result = str(get_memory())

            elif tool_name == "create_pomodoro":
                sessions = arguments.get("sessions", 1)
                tool_result = str(create_pomodoro(arguments["task"], sessions))

            elif tool_name == "save_completed_session":
                tool_result = save_completed_session(arguments["task"])

            elif tool_name == "get_statistics":
                tool_result = str(get_statistics())

            else:
                tool_result = "Unknown tool"

            print("Tool result:", tool_result)

            tool_outputs.append({
                "type": "function_call_output",
                "call_id": call_id,
                "output": str(tool_result)
            })

    if tool_outputs:
        final_response = client.responses.create(
            model="gpt-4o-mini",
            previous_response_id=response.id,
            input=tool_outputs
        )

        return final_response.output_text

    return response.output_text