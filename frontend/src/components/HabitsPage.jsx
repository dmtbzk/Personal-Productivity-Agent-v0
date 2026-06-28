import { useState, useEffect } from 'react'
import { fetchHabits, completeHabit } from '../api'
import './HabitsPage.css'

export default function HabitsPage() {
  const [habits, setHabits] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [completing, setCompleting] = useState(null)

  useEffect(() => { load() }, [])

  async function load() {
    try {
      setLoading(true)
      setError(null)
      setHabits(await fetchHabits())
    } catch {
      setError('Could not load habits. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }

  async function handleComplete(id) {
    setCompleting(id)
    try {
      await completeHabit(id)
      setHabits(await fetchHabits())
    } catch {
      setError('Failed to mark habit.')
    } finally {
      setCompleting(null)
    }
  }

  const completedToday = habits.filter(h => isToday(h.last_completed_at)).length
  const totalStreak = habits.reduce((sum, h) => sum + h.current_streak, 0)

  return (
    <div className="hp-page">
      <div className="hp-header">
        <div>
          <h1 className="hp-title">Habits</h1>
          <p className="hp-sub">Habits are added via the Chat page.</p>
        </div>
        <button className="hp-refresh" onClick={load} title="Refresh">↻</button>
      </div>

      {!loading && habits.length > 0 && (
        <div className="hp-stats">
          <div className="hp-stat">
            <span className="hp-stat-value">{completedToday}</span>
            <span className="hp-stat-label">done today</span>
          </div>
          <div className="hp-stat-divider" />
          <div className="hp-stat">
            <span className="hp-stat-value">{habits.length}</span>
            <span className="hp-stat-label">total habits</span>
          </div>
          <div className="hp-stat-divider" />
          <div className="hp-stat">
            <span className="hp-stat-value">{totalStreak}</span>
            <span className="hp-stat-label">combined streak</span>
          </div>
        </div>
      )}

      {error && <div className="hp-error">{error}</div>}

      {loading ? (
        <div className="hp-grid">
          {[1, 2, 3].map(i => <div key={i} className="hp-skeleton" />)}
        </div>
      ) : habits.length === 0 ? (
        <div className="hp-empty">
          <div className="hp-empty-icon">🌱</div>
          <p className="hp-empty-title">No habits yet</p>
          <p className="hp-empty-sub">Ask the agent to add a habit via Chat.</p>
        </div>
      ) : (
        <div className="hp-grid">
          {habits.map(habit => (
            <HabitCard
              key={habit.id}
              habit={habit}
              isCompleting={completing === habit.id}
              onComplete={handleComplete}
            />
          ))}
        </div>
      )}
    </div>
  )
}

function HabitCard({ habit, isCompleting, onComplete }) {
  const doneToday = isToday(habit.last_completed_at)

  return (
    <div className={`hp-card ${doneToday ? 'hp-card--done' : ''}`}>
      <div className="hp-card-top">
        <span className="hp-card-name">{habit.name}</span>
        {doneToday && <span className="hp-badge">Done</span>}
      </div>

      <div className="hp-card-meta">
        <div className="hp-streak">
          <span className="hp-streak-icon">🔥</span>
          <span className="hp-streak-val">{habit.current_streak}</span>
          <span className="hp-streak-label">day streak</span>
        </div>
        <span className="hp-total">{habit.completed_count}× total</span>
      </div>

      <div className="hp-week">
        <WeekDots habitId={habit.id} lastCompleted={habit.last_completed_at} streak={habit.current_streak} />
      </div>

      <button
        className={`hp-btn ${doneToday ? 'hp-btn--done' : ''}`}
        onClick={() => !doneToday && onComplete(habit.id)}
        disabled={doneToday || isCompleting}
      >
        {isCompleting ? '…' : doneToday ? '✓ Completed today' : 'Mark as done'}
      </button>
    </div>
  )
}

function WeekDots({ streak }) {
  const days = ['M', 'T', 'W', 'T', 'F', 'S', 'S']
  const todayIdx = (new Date().getDay() + 6) % 7

  return (
    <div className="hp-dots">
      {days.map((d, i) => {
        const daysAgo = todayIdx - i
        const filled = daysAgo >= 0 && daysAgo < streak
        return (
          <div key={i} className="hp-dot-col">
            <div className={`hp-dot ${filled ? 'hp-dot--filled' : ''} ${i === todayIdx ? 'hp-dot--today' : ''}`} />
            <span className="hp-dot-label">{d}</span>
          </div>
        )
      })}
    </div>
  )
}

function isToday(dateStr) {
  if (!dateStr) return false
  const d = new Date(dateStr)
  const now = new Date()
  return d.getFullYear() === now.getFullYear() &&
    d.getMonth() === now.getMonth() &&
    d.getDate() === now.getDate()
}
