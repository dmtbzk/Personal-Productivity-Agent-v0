from app.database.connection import get_connection


def save_conversation_message(role: str, content: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversation_messages (role, content)
        VALUES (?, ?)
        """,
        (role, content)
    )

    conn.commit()
    conn.close()


def get_recent_conversation_messages(limit: int = 10):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, content, created_at
        FROM conversation_messages
        ORDER BY id DESC
        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "role": row[0],
            "content": row[1],
            "created_at": row[2],
        }
        for row in reversed(rows)
    ]