# 🧠 Personal Productivity Agent

> I wanted to understand how modern AI agents actually work.  
> So I built one from scratch.

**Personal Productivity Agent** is a modular AI agent architecture built with **Python, FastAPI, OpenAI Responses API, SQLite, and React**.

This is not just a chatbot.  
It is a tool-using, memory-aware, context-driven personal productivity agent.

---

## ✨ Highlights

- 🧠 **LLM Planner** — understands user intent and selects the right tools
- 🧩 **Context Builder** — injects only relevant context into the model
- 🛠️ **Tool Calling** — executes real backend functions
- 🧰 **Tool Filtering** — the model only sees tools allowed by the planner
- 💾 **SQLite Persistence** — todos, memory, habits, calendar and conversations are stored
- 🧠 **Long-Term Memory** — stores stable user facts, routines, goals and preferences
- 💬 **Conversation Memory** — remembers recent messages for follow-up understanding
- ✅ **Todo Manager** — add, list, complete and delete tasks
- 🔁 **Habit Tracker** — habit progress, streaks and duplicate protection
- 📅 **Calendar Module** — schedule and list upcoming events
- 📊 **Statistics Module** — track completed focus sessions
- 🧱 **Modular Architecture** — planner, executor, responder, context and tools are separated
- ⚛️ **React Frontend** — planned as the user-facing interface

---

## 🚫 No Framework Magic

This project does **not** use:

- LangChain
- CrewAI
- AutoGen

Everything is built manually to understand the real architecture behind AI agents.

---

## 🧭 Why I Built This

Most AI tutorials stop at:

```text
User → LLM → Response