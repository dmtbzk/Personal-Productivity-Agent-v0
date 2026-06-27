from app.database.connection import get_connection


def save_completed_session(task: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO completed_sessions (task)
        VALUES (?)
        """,
        (task,)
    )

    conn.commit()
    conn.close()

    return f"Completed session saved: {task}"


def get_statistics():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, task, created_at
        FROM completed_sessions
    """)

    rows = cursor.fetchall()
    conn.close()

    return {
        "completed_sessions": len(rows),
        "tasks": [
            {
                "id": row[0],
                "task": row[1],
                "created_at": row[2]
            }
            for row in rows
        ]
    }