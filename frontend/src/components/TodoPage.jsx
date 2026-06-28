import { useState, useEffect } from 'react'
import { fetchTodos, updateTodoStatus, deleteTodo } from '../api'
import './TodoPage.css'

const COLUMNS = [
  { key: 'todo',        label: 'To Do',       accent: '#6b7280' },
  { key: 'in_progress', label: 'In Progress',  accent: '#f59e0b' },
  { key: 'done',        label: 'Done',         accent: '#22c55e' },
]

const NEXT_STATUS = { todo: 'in_progress', in_progress: 'done', done: null }

export default function TodoPage() {
  const [todos, setTodos] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => { load() }, [])

  async function load() {
    try {
      setLoading(true)
      setError(null)
      setTodos(await fetchTodos())
    } catch {
      setError('Could not load tasks. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }

  async function handleMove(id, newStatus) {
    setTodos(prev => prev.map(t => t.id === id ? { ...t, status: newStatus, done: newStatus === 'done' } : t))
    try {
      await updateTodoStatus(id, newStatus)
    } catch {
      load()
    }
  }

  async function handleDelete(id) {
    setTodos(prev => prev.filter(t => t.id !== id))
    try {
      await deleteTodo(id)
    } catch {
      load()
    }
  }

  const total = todos.length
  const doneCount = todos.filter(t => t.status === 'done').length
  const progress = total > 0 ? Math.round((doneCount / total) * 100) : 0

  return (
    <div className="tp-page">

      <div className="tp-header">
        <div>
          <h1 className="tp-title">Tasks</h1>
          <p className="tp-sub">Tasks are added via the Chat page.</p>
        </div>
        <button className="tp-refresh" onClick={load} title="Refresh">↻</button>
      </div>

      {total > 0 && (
        <div className="tp-progress-wrap">
          <div className="tp-progress-info">
            <span className="tp-progress-label">{doneCount} of {total} completed</span>
            <span className="tp-progress-pct">{progress}%</span>
          </div>
          <div className="tp-progress-bar">
            <div className="tp-progress-fill" style={{ width: `${progress}%` }} />
          </div>
        </div>
      )}

      {error && <div className="tp-error">{error}</div>}

      {loading ? (
        <div className="tp-board">
          {COLUMNS.map(col => (
            <div key={col.key} className="tp-col">
              <div className="tp-col-head">
                <div className="tp-skeleton tp-skeleton--title" />
              </div>
              <div className="tp-col-body">
                {[1, 2].map(i => <div key={i} className="tp-skeleton tp-skeleton--card" />)}
              </div>
            </div>
          ))}
        </div>
      ) : (
        <div className="tp-board">
          {COLUMNS.map(col => {
            const items = todos.filter(t => t.status === col.key)
            return (
              <div key={col.key} className="tp-col">
                <div className="tp-col-head">
                  <span className="tp-col-dot" style={{ background: col.accent }} />
                  <span className="tp-col-label">{col.label}</span>
                  <span className="tp-col-count">{items.length}</span>
                </div>
                <div className="tp-col-body">
                  {items.length === 0 ? (
                    <div className="tp-empty">No tasks here</div>
                  ) : (
                    items.map(todo => (
                      <TaskCard
                        key={todo.id}
                        todo={todo}
                        nextStatus={NEXT_STATUS[col.key]}
                        onMove={handleMove}
                        onDelete={handleDelete}
                      />
                    ))
                  )}
                </div>
              </div>
            )
          })}
        </div>
      )}
    </div>
  )
}

function TaskCard({ todo, nextStatus, onMove, onDelete }) {
  return (
    <div className="tp-card">
      <p className="tp-card-text">{todo.task}</p>
      <div className="tp-card-actions">
        {nextStatus && (
          <button
            className="tp-btn tp-btn--move"
            onClick={() => onMove(todo.id, nextStatus)}
          >
            {nextStatus === 'in_progress' ? '▶ Start' : '✓ Done'}
          </button>
        )}
        <button
          className="tp-btn tp-btn--delete"
          onClick={() => onDelete(todo.id)}
          aria-label="Delete"
        >
          ✕
        </button>
      </div>
    </div>
  )
}
