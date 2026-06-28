# Personal Productivity Agent

> I wanted to understand how modern AI agents actually work.  
> So I built one from scratch.

Personal Productivity Agent is an AI agent architecture built with **Python, FastAPI, OpenAI Responses API, SQLite, and React**.

This is not just a chatbot.

It is a modular AI agent system with:

- LLM-based planning
- tool calling
- context building
- conversation memory
- long-term memory
- habit tracking
- calendar management
- productivity statistics
- SQLite persistence
- React frontend

No LangChain.  
No CrewAI.  
No AutoGen.

Everything is built manually to understand the core architecture behind modern AI agents.

---

## Why I Built This

Most AI tutorials show how to call an LLM.

But real agents need more than that.

They need to:

- understand user intent
- decide which tools are needed
- retrieve relevant context
- remember previous conversations
- store long-term facts
- execute tools safely
- persist user data
- recover from planner failures
- return useful final answers

I built this project to learn and demonstrate those layers from scratch.

---

## Architecture

```text
                    User
                      │
                      ▼
                React Frontend
                      │
                      ▼
                 FastAPI Backend
                      │
                      ▼
                Orchestrator
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
   LLM Planner   Context Builder   Responder
        │             │             │
        │             ▼             ▼
        │      Combined Context   OpenAI Model
        │             │             │
        └─────────────┴─────────────┘
                      │
                      ▼
              Function Calling
                      │
                      ▼
                 Executor
                      │
                      ▼
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
      Todos        Memory        Calendar
        ▼             ▼             ▼
      Habits     Statistics   Conversation
                      │
                      ▼
                    SQLite