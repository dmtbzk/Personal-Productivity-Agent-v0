TOOLS = [
    {
        "type": "function",
        "name": "add_todo",
        "description": "Adds a new task to the user's todo list. Use this when the user wants to remember, add, or track a task.",
        "parameters": {
            "type": "object",
            "properties": {
                "task": {
                    "type": "string",
                    "description": "The task to add to the todo list."
                }
            },
            "required": ["task"]
        }
    },
    {
        "type": "function",
        "name": "list_todos",
        "description": "Returns the user's current todo list. Use this when the user asks what tasks they have or wants to review their todo list.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "type": "function",
        "name": "complete_todo",
        "description": "Marks a todo item as completed by its index. Use this when the user says they finished a task.",
        "parameters": {
            "type": "object",
            "properties": {
                "index": {
                    "type": "integer",
                    "description": "The zero-based index of the todo item to complete."
                }
            },
            "required": ["index"]
        }
    },
    {
        "type": "function",
        "name": "save_memory",
        "description": "Saves an important long-term note about the user, their goals, preferences, or working style.",
        "parameters": {
            "type": "object",
            "properties": {
                "note": {
                    "type": "string",
                    "description": "The memory note to save."
                }
            },
            "required": ["note"]
        }
    },
    {
        "type": "function",
        "name": "get_memory",
        "description": "Returns saved notes about the user. Use this when personal context would help answer better.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "type": "function",
        "name": "create_pomodoro",
        "description": "Creates a Pomodoro focus plan for a task. Use this when the user wants to focus, study, work deeply, or start a task.",
        "parameters": {
            "type": "object",
            "properties": {
                "task": {
                    "type": "string",
                    "description": "The task the user wants to focus on."
                },
                "sessions": {
                    "type": "integer",
                    "description": "Number of Pomodoro sessions."
                }
            },
            "required": ["task"]
        }
    },
    {
        "type": "function",
        "name": "save_completed_session",
        "description": "Saves a completed focus or Pomodoro session. Use this when the user says they completed a work session.",
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
    }
]