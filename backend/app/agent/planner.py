from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()

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

        "reasons": []
    }

    # --------------------
    # Todo
    # --------------------

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

        plan["reasons"].append("Todo management")

    # --------------------
    # Memory
    # --------------------

    if any(word in message for word in [
        "remember",
        "goal",
        "routine",
        "preference",
        "wake up",
        "name"
    ]):

        plan["context"]["memory"] = True

        plan["allowed_tools"] += [
            "save_memory",
            "get_memory"
        ]

        plan["reasons"].append("Memory lookup")

    # --------------------
    # Pomodoro
    # --------------------

    if any(word in message for word in [
        "pomodoro",
        "focus",
        "study"
    ]):

        plan["allowed_tools"].append("create_pomodoro")
        plan["reasons"].append("Focus planning")

    # --------------------
    # Statistics
    # --------------------

    if any(word in message for word in [
        "statistics",
        "progress",
        "completed"
    ]):

        plan["context"]["statistics"] = True

        plan["allowed_tools"] += ["get_statistics","save_completed_session"]

        plan["reasons"].append("Statistics lookup")

    # --------------------
    # Habits
    # --------------------

    if any(word in message for word in [
        "habit",
        "track",
        "streak",
        "daily",
        "routine"
    ]):
        plan["context"]["habits"] = True
        plan["allowed_tools"] += [
        "add_habit",
        "list_habits",
        "complete_habit"
        ]

        plan["reasons"].append("Habit tracking")

    # --------------------
    # Calendar
    # --------------------

    
    if any(word in message for word in [
        "calendar",
        "meeting",
        "appointment",
        "schedule",
        "event",
        "deadline",
        "tomorrow",
        "today at",
        "next week",
        "remind"
    ]):
        plan["context"]["calendar"] = True

        plan["allowed_tools"] += [
            "add_calendar_event",
            "list_calendar_events",
            "delete_calendar_event"
        ]

        plan["reasons"].append("Calendar management")



    return plan

def create_llm_plan(user_message: str):
    response = client.responses.create(
        model="gpt-4o-mini",
        input=[
            {
                "role": "system",
                "content": """
                You are the planner for a personal productivity agent.

                Your job is NOT to answer the user.
                Your job is to return a JSON plan.

                Return ONLY valid JSON. No markdown. No explanation.

                Available context sources:
                - memory
                - todos
                - statistics
                - calendar
                - habits

                Available tools:
                - add_todo
                - list_todos
                - complete_todo
                - delete_todo
                - save_memory
                - get_memory
                - create_pomodoro
                - save_completed_session
                - get_statistics
                - add_habit
                - list_habits
                - complete_habit
                - add_calendar_event
                - list_calendar_events
                - delete_calendar_event

                Rules:
                Memory rules:
                - Use get_memory only if answering requires previously saved personal information.
                - Use save_memory only if the user explicitly asks you to remember something, or they provide a long-term fact about themselves.
                - Do NOT use save_memory for temporary conversation details.

                Todo rules:
                - Use add_todo only when the user wants to create a task.
                - Use list_todos when the user asks what to do, wants to prioritize work, or asks about existing tasks.
                - Do not allow add_todo unless a new task is actually requested.

                Statistics rules:
                - Use save_completed_session only when the user explicitly says they finished or completed a work session.
                - Use get_statistics only when the user asks about progress or productivity.

                Habit rules:
                - Use add_habit only when creating a new habit.
                - Use complete_habit only when the user says they completed a habit.
                - Use list_habits only when the user asks about their habits.

                Calendar rules:
                - Use add_calendar_event only when the user wants to schedule a new event.
                - Use delete_calendar_event only when they ask to remove an event.
                - Use list_calendar_events only when they ask about their schedule or events.

                Return exactly this JSON shape:
                {
                "intent": "string",
                "context": {
                    "memory": false,
                    "todos": false,
                    "statistics": false,
                    "calendar": false,
                    "habits": false
                },
                "allowed_tools": [],
                "reasons": []
                }
                """
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    try:
        return json.loads(response.output_text)

    except Exception as error:
        print("LLM planner failed:", error)
        print("Raw planner output:", response.output_text)

        return create_plan(user_message)

