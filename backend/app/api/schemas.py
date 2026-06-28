from pydantic import BaseModel
from typing import Literal


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    answer: str


class TodoCreate(BaseModel):
    task: str


class TodoStatusUpdate(BaseModel):
    status: Literal["todo", "in_progress", "done"]


class TodoItem(BaseModel):
    id: int
    task: str
    done: bool
    status: str
