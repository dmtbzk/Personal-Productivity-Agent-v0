from openai import OpenAI
from dotenv import load_dotenv
import json

from app.tool_registry import TOOLS

from app.tools.todo import add_todo, list_todos, complete_todo, delete_todo
from app.tools.memory import save_memory, get_memory
from app.tools.pomodoro import create_pomodoro
from app.tools.statistics import save_completed_session, get_statistics
from app.tool_dispatcher import run_tool

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

            tool_result = run_tool(tool_name, arguments)

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