from app.database.connection import get_connection


def add_habit(name: str):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT id
        FROM habits
        WHERE LOWER(name) = LOWER(?)
        """,
        (name,)
    )

    existing_habit = cursor.fetchone()

    if existing_habit:
        conn.close()

    return f"Habit already exists: {name}"
    cursor.execute(
        """
        INSERT INTO habits (name)
        VALUES (?)
        """,
        (name,)
    )

    conn.commit()
    conn.close()

    return f"Habit added: {name}"


def list_habits():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            habits.id,
            habits.name,
            habits.created_at,
            COUNT(habit_logs.id) AS completed_count,
            MAX(habit_logs.completed_at) AS last_completed_at
        FROM habits
        LEFT JOIN habit_logs
            ON habits.id = habit_logs.habit_id
        GROUP BY habits.id
    """)

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "name": row[1],
            "created_at": row[2],
            "completed_count": row[3],
            "last_completed_at": row[4],
        }
        for row in rows
    ]


def complete_habit(habit_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM habit_logs
        WHERE habit_id = ?
          AND DATE(completed_at) = DATE('now')
        """,
        (habit_id,)
    )

    existing_log = cursor.fetchone()

    if existing_log:
        conn.close()
        return f"Habit already completed today: {habit_id}"

    cursor.execute(
        """
        INSERT INTO habit_logs (habit_id)
        VALUES (?)
        """,
        (habit_id,)
    )

    conn.commit()
    conn.close()

    return f"Habit completed: {habit_id}"