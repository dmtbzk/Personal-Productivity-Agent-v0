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
    {   "type": "function",
        "name": "delete_todo",
        "description": "Deletes a todo item by its id. Use this when the user wants to remove or delete a task.",
        "parameters": {
            "type": "object",
            "properties": {
                "index": {
                    "type": "integer",
                    "description": "The id of the todo item to delete."
                }
            },
            "required": ["index"]
        }
    },
   {
        "type": "function",
        "name": "save_memory",
        "description": "Saves structured long-term memory about the user. Use this when the user tells the assistant something important about their profile, goals, preferences, habits, routines, or working style.",
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
        "description": "Returns saved notes about the user. Use this when personal context would help answer better.",
        "parameters": {
            "type": "object",
            "properties": {},
            "required": []
        }
    },
    {
        "type": "function",
        "name": "search_memory",
        "description": "Searches for saved notes about the user. Use this when the user asks for information about their profile, goals, preferences, habits, routines, or working style.",
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