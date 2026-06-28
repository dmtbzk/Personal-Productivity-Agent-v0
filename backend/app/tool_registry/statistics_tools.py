STATISTICS_TOOLS = [
    {
        "type": "function",
        "name": "save_completed_session",
        "description": "Saves a completed focus or Pomodoro session. Use this only when the user explicitly says they completed a work or focus session.",
        "parameters": {
            "type": "object",
            "properties": {
                "task": {
                    "type": "string",
                    "description": "The task completed during the session."
                }
            },
            "required": ["task"]
        }
    },
    {
        "type": "function",
        "name": "get_statistics",
        "description": "Returns productivity statistics such as completed focus sessions.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
]