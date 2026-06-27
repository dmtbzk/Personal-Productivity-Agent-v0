from openai import OpenAI
from dotenv import load_dotenv

from app.tool_registry import get_allowed_tools

load_dotenv()

client = OpenAI()


def create_initial_response(system_prompt: str, user_message: str, allowed_tool_names: list[str]):
    allowed_tools = get_allowed_tools(allowed_tool_names)

    return client.responses.create(
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
        tools=allowed_tools
    )

def create_final_response(previous_response_id: str, tool_outputs: list):
    return client.responses.create(
        model="gpt-4o-mini",
        previous_response_id=previous_response_id,
        input=tool_outputs
    )