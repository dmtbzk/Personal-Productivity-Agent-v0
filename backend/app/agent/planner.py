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
                - If the user is greeting or casual chatting, allow no tools.
                - If the user asks what to work on, plan their day, prioritize, or organize work, include todos.
                - If the user mentions routines, preferences, goals, name, wake-up time, or asks based on personal info, include memory.
                - If the user asks about progress, completed sessions, stats, or performance, include statistics.
                - If the user asks about habits, streaks, daily actions, or tracking habits, include habits.
                - If the user asks about schedule, meetings, appointments, deadlines, events, or calendar, include calendar.
                - Only allow tools relevant to the request.

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

