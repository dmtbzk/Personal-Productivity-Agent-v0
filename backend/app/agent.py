from openai import OpenAI
from dotenv import load_dotenv
import json

from app.tool_registry import TOOLS
from app.tools.memory import search_memory
from app.tool_dispatcher import run_tool

load_dotenv()

client = OpenAI()


def run_agent(user_message: str) -> str:
    relevant_memories = search_memory(user_message)

    system_prompt = f"""
You are a personal productivity assistant.

Use the user's saved memory when it is relevant.
Do not mention memory unless it helps the answer.

Relevant user memory:
{relevant_memories}
"""

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_message
            }
        ],
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