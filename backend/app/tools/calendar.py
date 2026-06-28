from app.database.connection import get_connection


def add_calendar_event(
    title: str,
    event_date: str,
    event_time: str = "",
    description: str = ""
):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO calendar_events (
            title,
            event_date,
            event_time,
            description
        )
        VALUES (?, ?, ?, ?)
        """,
        (title, event_date, event_time, description)
    )

    conn.commit()
    conn.close()

    return f"Calendar event added: {title} on {event_date} at {event_time}"


def list_calendar_events():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id, title, event_date, event_time, description, created_at
        FROM calendar_events
        ORDER BY event_date ASC, event_time ASC
        """
    )

    rows = cursor.fetchall()
    conn.close()

    return [
        {
            "id": row[0],
            "title": row[1],
            "event_date": row[2],
            "event_time": row[3],
            "description": row[4],
            "created_at": row[5],
        }
        for row in rows
    ]


def delete_calendar_event(event_id: int):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM calendar_events
        WHERE id = ?
        """,
        (event_id,)
    )

    conn.commit()
    conn.close()

    return f"Calendar event deleted: {event_id}"