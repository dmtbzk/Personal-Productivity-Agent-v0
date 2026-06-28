from pydantic import BaseModel
from typing import Literal, Optional


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str



class TodoStatusUpdate(BaseModel):
    status: Literal["todo", "in_progress", "done"]


class TodoItem(BaseModel):
    id: int
    task: str
    done: bool
    status: str


class StatsResponse(BaseModel):
    total_todos: int
    completed_todos: int
    in_progress_todos: int
    total_habits: int
    total_habit_completions: int
    total_sessions: int
    sessions_by_day: dict
    recent_sessions: list


class CalendarEvent(BaseModel):
    id: int
    title: str
    event_date: str
    event_time: Optional[str]
    description: Optional[str]
    created_at: str


class HabitItem(BaseModel):
    id: int
    name: str
    created_at: str
    completed_count: int
    last_completed_at: Optional[str]
    current_streak: int
