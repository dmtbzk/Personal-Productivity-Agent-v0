def create_pomodoro(task: str, sessions: int = 1):
    return {
        "task": task,
        "sessions": sessions,
        "structure": "25 minutes focus + 5 minutes break"
    }