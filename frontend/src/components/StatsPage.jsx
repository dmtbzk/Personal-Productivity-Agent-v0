import { useState, useEffect } from 'react'
import { fetchStats } from '../api'
import './StatsPage.css'

export default function StatsPage() {
  const [stats, setStats]   = useState(null)
  const [loading, setLoading] = useState(true)
  const [error, setError]   = useState(null)

  useEffect(() => { load() }, [])

  async function load() {
    try {
      setLoading(true); setError(null)
      setStats(await fetchStats())
    } catch {
      setError('Could not load statistics. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="sp-page">
      <div className="sp-header">
        <div>
          <h1 className="sp-title">Statistics</h1>
          <p className="sp-sub">Your productivity at a glance.</p>
        </div>
        <button className="sp-refresh" onClick={load} title="Refresh">↻</button>
      </div>

      {error && <div className="sp-error">{error}</div>}

      {loading ? <LoadingSkeleton /> : stats && <Dashboard stats={stats} />}
    </div>
  )
}

function Dashboard({ stats }) {
  const total = stats.total_todos || 1
  const pctDone       = Math.round((stats.completed_todos   / total) * 100)
  const pctInProgress = Math.round((stats.in_progress_todos / total) * 100)
  const pctTodo       = 100 - pctDone - pctInProgress

  const cards = [
    { label: 'Total tasks',       value: stats.total_todos,             color: 'blue' },
    { label: 'Completed tasks',   value: stats.completed_todos,         color: 'green' },
    { label: 'In progress',       value: stats.in_progress_todos,       color: 'amber' },
    { label: 'Active habits',     value: stats.total_habits,            color: 'purple' },
    { label: 'Habit check-ins',   value: stats.total_habit_completions, color: 'teal' },
    { label: 'Focus sessions',    value: stats.total_sessions,          color: 'coral' },
  ]

  return (
    <div className="sp-dashboard">
      {/* metric cards */}
      <div className="sp-cards">
        {cards.map(c => (
          <div key={c.label} className={`sp-card sp-card--${c.color}`}>
            <span className="sp-card-value">{c.value}</span>
            <span className="sp-card-label">{c.label}</span>
          </div>
        ))}
      </div>

      {/* task progress */}
      <div className="sp-section">
        <p className="sp-section-label">Task completion</p>
        <div className="sp-progress-card">
          <div className="sp-progress-top">
            <span className="sp-progress-text">
              {stats.completed_todos} of {stats.total_todos} tasks done
            </span>
            <span className="sp-progress-pct">{pctDone}%</span>
          </div>
          <div className="sp-bar">
            <div className="sp-bar-fill sp-bar-fill--green" style={{ width: `${pctDone}%` }} />
            <div className="sp-bar-fill sp-bar-fill--amber" style={{ width: `${pctInProgress}%` }} />
            <div className="sp-bar-fill sp-bar-fill--gray"  style={{ width: `${pctTodo}%` }} />
          </div>
          <div className="sp-bar-legend">
            <span className="sp-legend-dot sp-legend-dot--green" />Done
            <span className="sp-legend-dot sp-legend-dot--amber" />In progress
            <span className="sp-legend-dot sp-legend-dot--gray"  />To do
          </div>
        </div>
      </div>

      {/* sessions chart */}
      <div className="sp-section">
        <p className="sp-section-label">Focus sessions — last 14 days</p>
        <div className="sp-chart-card">
          <SessionsChart sessionsByDay={stats.sessions_by_day} />
        </div>
      </div>

      {/* recent sessions */}
      {stats.recent_sessions.length > 0 && (
        <div className="sp-section">
          <p className="sp-section-label">Recent sessions</p>
          <div className="sp-list">
            {stats.recent_sessions.map(s => (
              <div key={s.id} className="sp-list-row">
                <span className="sp-list-task">{s.task}</span>
                <span className="sp-list-date">{formatDate(s.created_at)}</span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

function SessionsChart({ sessionsByDay }) {
  const days = last14Days()
  const max  = Math.max(...days.map(d => sessionsByDay[d] || 0), 1)

  return (
    <div className="sp-chart">
      {days.map(day => {
        const count  = sessionsByDay[day] || 0
        const height = Math.round((count / max) * 100)
        const isToday = day === todayStr()
        return (
          <div key={day} className="sp-bar-col">
            <span className="sp-bar-count">{count > 0 ? count : ''}</span>
            <div className="sp-bar-track">
              <div
                className={`sp-bar-inner ${isToday ? 'sp-bar-inner--today' : ''}`}
                style={{ height: `${height}%` }}
              />
            </div>
            <span className={`sp-bar-day ${isToday ? 'sp-bar-day--today' : ''}`}>
              {shortDay(day)}
            </span>
          </div>
        )
      })}
    </div>
  )
}

function LoadingSkeleton() {
  return (
    <div className="sp-dashboard">
      <div className="sp-cards">
        {Array.from({ length: 6 }).map((_, i) => (
          <div key={i} className="sp-skeleton sp-skeleton--card" />
        ))}
      </div>
      <div className="sp-skeleton sp-skeleton--wide" />
      <div className="sp-skeleton sp-skeleton--wide" />
    </div>
  )
}

// helpers
function todayStr() {
  return new Date().toISOString().slice(0, 10)
}

function last14Days() {
  return Array.from({ length: 14 }, (_, i) => {
    const d = new Date()
    d.setDate(d.getDate() - 13 + i)
    return d.toISOString().slice(0, 10)
  })
}

function shortDay(dateStr) {
  const d = new Date(dateStr + 'T00:00')
  return d.toLocaleDateString('en-US', { weekday: 'short' }).slice(0, 1)
}

function formatDate(str) {
  return new Date(str).toLocaleDateString('en-US', { month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
}
