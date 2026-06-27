from app.database.connection import get_connection
from datetime import datetime, timedelta

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


def calculate_streak(completed_dates):

    if not completed_dates:
        return 0

    unique_dates = sorted(
        set(completed_dates),
        reverse=True
    )

    today = datetime.now().date()
    streak = 0

    for date_value in unique_dates:
        completed_date = datetime.strptime(date_value, "%Y-%m-%d").date()
        expected_date = today - timedelta(days=streak)
        if completed_date == expected_date:
            streak += 1
        else:
            break

    return streak

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

    habit_rows = cursor.fetchall()

    habits = []

    for habit in habit_rows:
        habit_id = habit[0]

        cursor.execute(
            """
            SELECT DATE(completed_at)
            FROM habit_logs
            WHERE habit_id = ?
            ORDER BY completed_at DESC
            """,
            (habit_id,)
        )

        completed_dates = [
            row[0]
            for row in cursor.fetchall()
        ]

        habits.append({
            "id": habit[0],
            "name": habit[1],
            "created_at": habit[2],
            "completed_count": habit[3],
            "last_completed_at": habit[4],
            "current_streak": calculate_streak(completed_dates),
        })

    conn.close()

    return habits


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