from app.agent.responder import (
    create_initial_response,
    create_final_response,
)
from app.agent.executor import execute_tool_calls
from app.context.context_builder import build_context
from app.agent.planner import create_plan


def run(user_message: str) -> str:
    plan = create_plan(user_message)
    print("Plan:", plan)

    context = build_context(plan, user_message)

    system_prompt = f"""
    You are a personal productivity assistant.

    Use the user's saved memory when it is relevant.
    Do not mention memory unless it helps the answer.

    For calendar events:
    - If the user gives a relative date like "tomorrow", "next week", or "Friday", do not guess the exact date.
    - Ask the user for the exact date in YYYY-MM-DD format.
    - Only call calendar tools when event_date is an exact YYYY-MM-DD date.

    Planner reasons:
    {plan["reasons"]}

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