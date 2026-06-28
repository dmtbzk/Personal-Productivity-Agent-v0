# 🧠 Personal Productivity Agent

<p align="center">

Python
FastAPI
React
TypeScript
SQLite
OpenAI

</p>

<p align="center">

A modular AI Agent built from scratch using Python, FastAPI, OpenAI Responses API and React.

No LangChain • No CrewAI • No AutoGen

</p>

---

## 🚀 About

Most AI tutorials stop here:

text User    │    ▼ OpenAI API    │    ▼ Response 

Real AI agents are far more sophisticated.

They need to:

- understand the user's intent
- retrieve the correct context
- remember previous conversations
- manage long-term memory
- choose the right tools
- execute backend functions
- persist data
- generate grounded responses

This project was built to understand and implement those layers manually instead of relying on existing AI agent frameworks.

The goal is not simply to build a chatbot.

The goal is to build the architecture behind one.

---

# ✨ Features

## 🧠 AI Agent

- Intent-based LLM Planner
- Dynamic Tool Selection
- Tool Calling via OpenAI Responses API
- Context-Aware Responses
- Conversation Memory
- Long-Term Memory
- Function Execution Pipeline
- Modular AI Architecture

---

## 📋 Productivity

- Todo Management
- Habit Tracking
- Calendar Events
- Productivity Statistics
- Daily Planning
- Focus Session Tracking

---

## 💾 Memory

- Structured Long-Term Memory
- Conversation History
- Memory Search
- Context Injection
- User Preferences
- Goals & Routines

---

## 🏗 Backend

- FastAPI REST API
- SQLite Persistence
- Modular Service Layer
- Tool Registry
- Context Builder
- Planner
- Executor
- Responder
- Orchestrator

---

## 🎨 Frontend (In Progress)

- React
- TypeScript
- Vite
- Modern Dashboard
- Chat Interface
- Productivity Panels
- Agent Debug View

---

# 🏛 Architecture

text                            User                              │                              ▼                     React Frontend                              │                              ▼                      FastAPI Backend                              │                              ▼                       Orchestrator                              │         ┌────────────────────┼────────────────────┐         ▼                    ▼                    ▼   LLM Planner         Context Builder        Responder         │                    │                    │         │                    ▼                    ▼         │            Combined Context      OpenAI Responses API         │                    │                    │         └────────────────────┴────────────────────┘                              │                              ▼                       Function Calling                              │                              ▼                           Executor                              │          ┌───────────────────┼───────────────────┐          ▼                   ▼                   ▼       Todos             Long-Term Memory     Calendar          ▼                   ▼                   ▼       Habits           Conversation DB     Statistics                              │                              ▼                           SQLite 

---

# 🎯 Design Principles

This project follows a modular architecture where every component has a single responsibility.

| Component | Responsibility |
|-----------|----------------|
| Planner | Understands user intent |
| Context Builder | Collects only relevant context |
| Tool Registry | Describes available tools |
| Executor | Executes Python functions |
| Responder | Generates the final response |
| Services | Business logic |
| SQLite | Persistent storage |

---

# 🔥 Current Capabilities

- ✅ Understand user intent
- ✅ Select relevant tools automatically
- ✅ Filter available tools
- ✅ Execute backend functions
- ✅ Persist user data
- ✅ Remember previous conversations
- ✅ Store long-term memory
- ✅ Track productivity
- ✅ Manage habits
- ✅ Manage calendar events
- ✅ Plan daily work
- ✅ Track focus sessions

---

> "I wanted to understand how ChatGPT-like agents work internally, so I built one layer by layer instead of hiding everything behind a framework."