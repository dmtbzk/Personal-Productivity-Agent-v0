MEMORY_TOOLS = [
    {
        "type": "function",
        "name": "save_memory",
        "description": "Saves structured long-term memory about the user. Use this only when the user explicitly asks to remember something or states a stable personal fact, goal, preference, habit, routine, or working style.",
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "The memory category, for example: profile, preference, goal, habit, routine, working_style."
                },
                "key": {
                    "type": "string",
                    "description": "The specific memory key, for example: name, city, wake_up_time, current_goal."
                },
                "value": {
                    "type": "string",
                    "description": "The memory value to save."
                }
            },
            "required": ["category", "key", "value"]
        }
    },
    {
        "type": "function",
        "name": "get_memory",
        "description": "Returns saved memory about the user. Use this when personal context is needed.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "type": "function",
        "name": "search_memory",
        "description": "Searches saved memory about the user.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The query to search for in the user's memory."
                }
            },
            "required": ["query"]
        }
    },
]