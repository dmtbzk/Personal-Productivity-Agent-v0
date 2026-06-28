from app.database.connection import get_connection


def _migrate_status(cursor):
    cols = [row[1] for row in cursor.execute("PRAGMA table_info(todos)").fetchall()]
    if "status" not in cols:
        cursor.execute("ALTER TABLE todos ADD COLUMN status TEXT DEFAULT 'todo'")
        cursor.execute("UPDATE todos SET status = 'done' WHERE done = 1")


def add_todo(task: str):
    conn = get_connection()
    cursor = conn.cursor()
    _migrate_status(cursor)
    cursor.execute(
        "INSERT INTO todos (task, done, status) VALUES (?, 0, 'todo')",
        (task,),
    )
    conn.commit()
    conn.close()
    return f"Todo added: {task}"


def list_todos():
    conn = get_connection()
    cursor = conn.cursor()
    _migrate_status(cursor)
    conn.commit()
    rows = cursor.execute("SELECT id, task, done, status FROM todos").fetchall()
    conn.close()
    return [
        {"id": row[0], "task": row[1], "done": bool(row[2]), "status": row[3] or "todo"}
        for row in rows
    ]


def update_todo_status(todo_id: int, status: str):
    conn = get_connection()
    cursor = conn.cursor()
    _migrate_status(cursor)
    done = 1 if status == "done" else 0
    cursor.execute(
        "UPDATE todos SET status = ?, done = ? WHERE id = ?",
        (status, done, todo_id),
    )
    conn.commit()
    conn.close()
    return f"Todo {todo_id} status updated to {status}"


def complete_todo(index: int):
    return update_todo_status(index, "done")


def delete_todo(index: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (index,))
    conn.commit()
    conn.close()
    return f"Todo deleted: {index}"
