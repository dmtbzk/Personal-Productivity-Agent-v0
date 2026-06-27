from fastapi import APIRouter

from app.api.schemas import ChatRequest, ChatResponse
from app.agent.orchestrator import run

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