from app.tools.todo import list_todos


def build_todo_context() -> str:
    todos = list_todos()

    if not todos:
        return "No todos found."

    pending_todos = [
        todo for todo in todos
        if todo["done"] is False
    ]

    if not pending_todos:
        return "No pending todos."

    return f"""
    Pending todos:
    {pending_todos}
    """