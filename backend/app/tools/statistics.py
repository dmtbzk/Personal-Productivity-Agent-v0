completed_sessions = []


def save_completed_session(task: str):
    completed_sessions.append(task)

    return f"Saved completed session for: {task}"


def get_statistics():
    return {
        "completed_sessions": len(completed_sessions),
        "tasks": completed_sessions
    }