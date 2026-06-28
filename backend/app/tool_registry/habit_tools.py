HABIT_TOOLS = [
    {
        "type": "function",
        "name": "add_habit",
        "description": "Adds a new habit for the user to track. Use this only when the user wants to create, start, or track a repeated habit.",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The habit name to add."
                }
            },
            "required": ["name"]
        }
    },
    {
        "type": "function",
        "name": "list_habits",
        "description": "Returns the user's tracked habits, including progress and streak information.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "type": "function",
        "name": "complete_habit",
        "description": "Marks a habit as completed by habit id. Use this only when the user says they completed or did a habit today.",
        "parameters": {
            "type": "object",
            "properties": {
                "habit_id": {
                    "type": "integer",
                    "description": "The id of the habit to mark as completed."
                }
            },
            "required": ["habit_id"]
        }
    },
]