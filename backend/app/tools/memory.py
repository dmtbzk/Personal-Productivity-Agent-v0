from app.database import get_connection


def normalize_category(category: str, key: str):
    mapping = {
        "name": "profile",
        "city": "profile",
        "country": "profile",

        "wake_up_time": "routine",
        "bed_time": "routine",
        "morning_routine": "routine",

        "favorite_food": "preference",
        "favorite_language": "preference",

        "career_goal": "goal",
        "learning_goal": "goal",
        "current_goal": "goal",
    }

    return mapping.get(key, category)


def save_memory(category: str, key: str, value: str):
    category = normalize_category(category, key)

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM memories
        WHERE category = ? AND key = ?
        """,
        (category, key)
    )

    existing_memory = cursor.fetchone()

    if existing_memory:
        cursor.execute(
            """
            UPDATE memories
            SET value = ?,
                updated_at = CURRENT_TIMESTAMP
            WHERE category = ? AND key = ?
            """,
            (value, category, key)
        )

        result = f"Memory updated: {category}.{key} = {value}"

    else:
        cursor.execute(
            """
            INSERT INTO memories (category, key, value)
            VALUES (?, ?, ?)
            """,
            (category, key, value)
        )

        result = f"Memory saved: {category}.{key} = {value}"

    conn.commit()
    conn.close()

    return result


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
    
def search_memory(query: str):
    conn = get_connection()
    cursor = conn.cursor()

    search_text = f"%{query}%"

    cursor.execute(
        """
        SELECT id, category, key, value, created_at, updated_at
        FROM memories
        WHERE category LIKE ?
           OR key LIKE ?
           OR value LIKE ?
        """,
        (search_text, search_text, search_text)
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