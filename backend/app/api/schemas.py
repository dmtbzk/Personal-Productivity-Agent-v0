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


class HabitItem(BaseModel):
    id: int
    name: str
    created_at: str
    completed_count: int
    last_completed_at: Optional[str]
    current_streak: int
