from openai import OpenAI
from dotenv import load_dotenv

from app.tool_registry import TOOLS

load_dotenv()

client = OpenAI()


def create_initial_response(system_prompt: str, user_message: str):
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
        tools=TOOLS
    )


def create_final_response(previous_response_id: str, tool_outputs: list):
    return client.responses.create(
        model="gpt-4o-mini",
        previous_response_id=previous_response_id,
        input=tool_outputs
    )