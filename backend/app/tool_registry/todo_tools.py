TODO_TOOLS = [
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
        "description": "Marks a todo item as completed by its id. Use this when the user says they finished a task.",
        "parameters": {
            "type": "object",
            "properties": {
                "index": {
                    "type": "integer",
                    "description": "The id of the todo item to complete."
                }
            },
            "required": ["index"]
        }
    },
    {
        "type": "function",
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
]