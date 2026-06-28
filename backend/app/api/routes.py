from fastapi import APIRouter

from app.api.schemas import ChatRequest, ChatResponse, TodoCreate, TodoStatusUpdate, TodoItem
from app.agent.orchestrator import run
from app.tools.todo import add_todo, list_todos, update_todo_status, delete_todo

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


@router.post("/todos", response_model=TodoItem)
def create_todo(body: TodoCreate):
    add_todo(body.task)
    return list_todos()[-1]


@router.patch("/todos/{todo_id}/status")
def update_status(todo_id: int, body: TodoStatusUpdate):
    update_todo_status(todo_id, body.status)
    return {"status": "ok"}


@router.delete("/todos/{todo_id}")
def delete_todo_route(todo_id: int):
    delete_todo(todo_id)
    return {"status": "ok"}
