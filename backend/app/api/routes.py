from fastapi import APIRouter

from app.api.schemas import ChatRequest, ChatResponse, TodoStatusUpdate, TodoItem, HabitItem, CalendarEvent, StatsResponse
from app.agent.orchestrator import run
from app.tools.todo import list_todos, update_todo_status, delete_todo
from app.tools.habits import list_habits, complete_habit
from app.tools.calendar import list_calendar_events, delete_calendar_event
from app.tools.statistics import get_statistics
from app.tools.habits import list_habits
from app.tools.todo import list_todos as _list_todos
from app.database.connection import get_connection

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Personal Productivity Agent API"}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    answer = run(request.message)
    return ChatResponse(answer=answer)


@router.get("/todos", response_model=list[TodoItem])
def get_todos():
    return list_todos()


@router.patch("/todos/{todo_id}/status")
def update_status(todo_id: int, body: TodoStatusUpdate):
    update_todo_status(todo_id, body.status)
    return {"status": "ok"}


@router.delete("/todos/{todo_id}")
def delete_todo_route(todo_id: int):
    delete_todo(todo_id)
    return {"status": "ok"}


@router.get("/habits", response_model=list[HabitItem])
def get_habits():
    return list_habits()


@router.post("/habits/{habit_id}/complete")
def complete_habit_route(habit_id: int):
    result = complete_habit(habit_id)
    return {"message": result}


@router.get("/stats", response_model=StatsResponse)
def get_stats():
    todos   = _list_todos()
    habits  = list_habits()
    raw     = get_statistics()

    sessions_by_day: dict[str, int] = {}
    for s in raw["tasks"]:
        day = s["created_at"][:10]
        sessions_by_day[day] = sessions_by_day.get(day, 0) + 1

    conn   = get_connection()
    cursor = conn.cursor()
    total_habit_completions = cursor.execute("SELECT COUNT(*) FROM habit_logs").fetchone()[0]
    conn.close()

    return StatsResponse(
        total_todos=len(todos),
        completed_todos=sum(1 for t in todos if t["status"] == "done"),
        in_progress_todos=sum(1 for t in todos if t["status"] == "in_progress"),
        total_habits=len(habits),
        total_habit_completions=total_habit_completions,
        total_sessions=raw["completed_sessions"],
        sessions_by_day=sessions_by_day,
        recent_sessions=raw["tasks"][-10:][::-1],
    )


@router.get("/calendar", response_model=list[CalendarEvent])
def get_calendar():
    return list_calendar_events()


@router.delete("/calendar/{event_id}")
def delete_event(event_id: int):
    delete_calendar_event(event_id)
    return {"status": "ok"}
