from app.tools.calendar import list_calendar_events


def build_calendar_context() -> str:
    events = list_calendar_events()

    if not events:
        return "No calendar events."

    return f"""
    Upcoming calendar events:
    {events}
    """