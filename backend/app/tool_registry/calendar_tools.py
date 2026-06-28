CALENDAR_TOOLS = [
    {
        "type": "function",
        "name": "add_calendar_event",
        "description": "Adds a calendar event. Use this when the user wants to schedule a meeting, appointment, deadline or event.",
        "parameters": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "The event title."
                },
                "event_date": {
                    "type": "string",
                    "description": "The event date in YYYY-MM-DD format."
                },
                "event_time": {
                    "type": "string",
                    "description": "Optional event time in HH:MM format."
                },
                "description": {
                    "type": "string",
                    "description": "Optional event description."
                }
            },
            "required": ["title", "event_date"]
        }
    },
    {
        "type": "function",
        "name": "list_calendar_events",
        "description": "Lists upcoming calendar events.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "type": "function",
        "name": "delete_calendar_event",
        "description": "Deletes a calendar event by its id.",
        "parameters": {
            "type": "object",
            "properties": {
                "event_id": {
                    "type": "integer",
                    "description": "The id of the event to delete."
                }
            },
            "required": ["event_id"]
        }
    }
]