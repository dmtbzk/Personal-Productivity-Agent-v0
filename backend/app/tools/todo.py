from app.database.connection import get_connection

todos = []

def add_todo(task: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO todos (task, done) VALUES (?, ?)", (task, False))
    conn.commit()
    conn.close()
    return f"Todo added: {task}"


def list_todos():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM todos")
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id": row[0],
            "task": row[1],
            "done": bool(row[2])
        }
        for row in rows
    ]

def complete_todo(index: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE todos SET done = 1 WHERE id = ?", (index,))
    conn.commit()
    conn.close()
    return f"Todo completed: {index}"

def delete_todo(index: int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = ?", (index,))
    conn.commit()
    conn.close()
    return f"Todo deleted: {index}"