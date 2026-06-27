from app.agent.responder import (
    create_initial_response,
    create_final_response,
)
from app.agent.executor import execute_tool_calls
from app.context.context_builder import build_context
from app.agent.planner import create_plan

def run(user_message: str) -> str:
    plan = create_plan(user_message)
    context = build_context(user_message)

    system_prompt = f"""
    You are a personal productivity assistant.

    Use the user's saved memory when it is relevant.
    Do not mention memory unless it helps the answer.

    {context}
    """

    response = create_initial_response(
        system_prompt,
        user_message,
        plan["allowed_tools"]
    )

    tool_outputs = execute_tool_calls(response)

    if tool_outputs:
        final_response = create_final_response(
            response.id,
            tool_outputs
        )
        return final_response.output_text

    return response.output_text