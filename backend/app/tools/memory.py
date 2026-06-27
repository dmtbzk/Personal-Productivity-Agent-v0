from app.database import get_connection


def save_memory(category: str, key: str, value: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO memories (category, key, value)
        VALUES (?, ?, ?)
        """,
        (category, key, value)
    )

    conn.commit()
    conn.close()

    return f"Memory saved: {category}.{key} = {value}"


def get_memory():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, category, key, value, created_at, updated_at
        FROM memories
        """
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "category": row[1],
            "key": row[2],
            "value": row[3],
            "created_at": row[4],
            "updated_at": row[5],
        }
        for row in rows
    ]