import { useState, useEffect } from 'react'
import { fetchCalendar, deleteEvent } from '../api'
import './CalendarPage.css'

const MONTHS = ['January','February','March','April','May','June',
                 'July','August','September','October','November','December']
const DAYS   = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

export default function CalendarPage() {
  const [events, setEvents]   = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError]     = useState(null)
  const [selected, setSelected] = useState(null) // 'YYYY-MM-DD'

  const today = new Date()
  const [viewYear,  setViewYear]  = useState(today.getFullYear())
  const [viewMonth, setViewMonth] = useState(today.getMonth())

  useEffect(() => { load() }, [])

  async function load() {
    try {
      setLoading(true); setError(null)
      setEvents(await fetchCalendar())
    } catch {
      setError('Could not load events. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }

  async function handleDelete(id) {
    setEvents(prev => prev.filter(e => e.id !== id))
    try { await deleteEvent(id) } catch { load() }
  }

  function prevMonth() {
    if (viewMonth === 0) { setViewYear(y => y - 1); setViewMonth(11) }
    else setViewMonth(m => m - 1)
  }
  function nextMonth() {
    if (viewMonth === 11) { setViewYear(y => y + 1); setViewMonth(0) }
    else setViewMonth(m => m + 1)
  }

  const eventsByDate = events.reduce((acc, e) => {
    acc[e.event_date] = acc[e.event_date] || []
    acc[e.event_date].push(e)
    return acc
  }, {})

  const todayStr    = fmtDate(today)
  const selectedEvents = selected ? (eventsByDate[selected] || []) : []

  // upcoming = from today, sorted
  const upcoming = events
    .filter(e => e.event_date >= todayStr)
    .sort((a, b) => (a.event_date + (a.event_time || '')).localeCompare(b.event_date + (b.event_time || '')))

  const cells = buildCells(viewYear, viewMonth)

  return (
    <div className="cp-page">
      <div className="cp-header">
        <div>
          <h1 className="cp-title">Calendar</h1>
          <p className="cp-sub">Events are added via the Chat page.</p>
        </div>
        <button className="cp-refresh" onClick={load} title="Refresh">↻</button>
      </div>

      {error && <div className="cp-error">{error}</div>}

      <div className="cp-layout">
        {/* ── left: mini calendar ── */}
        <div className="cp-left">
          <div className="cp-cal">
            <div className="cp-cal-nav">
              <button className="cp-nav-btn" onClick={prevMonth}>‹</button>
              <span className="cp-cal-label">{MONTHS[viewMonth]} {viewYear}</span>
              <button className="cp-nav-btn" onClick={nextMonth}>›</button>
            </div>
            <div className="cp-cal-grid">
              {DAYS.map(d => (
                <div key={d} className="cp-day-name">{d}</div>
              ))}
              {loading
                ? Array.from({ length: 35 }).map((_, i) => (
                    <div key={i} className="cp-cell cp-cell--skeleton" />
                  ))
                : cells.map((cell, i) => {
                    if (!cell) return <div key={i} className="cp-cell cp-cell--empty" />
                    const dateStr  = fmtDate(cell)
                    const hasEvent = !!eventsByDate[dateStr]
                    const isToday  = dateStr === todayStr
                    const isSel    = dateStr === selected
                    return (
                      <button
                        key={i}
                        className={[
                          'cp-cell',
                          isToday  ? 'cp-cell--today'    : '',
                          isSel    ? 'cp-cell--selected' : '',
                          hasEvent ? 'cp-cell--has-event': '',
                        ].join(' ')}
                        onClick={() => setSelected(isSel ? null : dateStr)}
                      >
                        {cell.getDate()}
                        {hasEvent && <span className="cp-dot" />}
                      </button>
                    )
                  })
              }
            </div>
          </div>

          {/* selected day panel */}
          {selected && (
            <div className="cp-day-panel">
              <p className="cp-day-panel-title">{formatDisplayDate(selected)}</p>
              {selectedEvents.length === 0 ? (
                <p className="cp-day-panel-empty">No events</p>
              ) : (
                selectedEvents.map(e => (
                  <EventRow key={e.id} event={e} onDelete={handleDelete} />
                ))
              )}
            </div>
          )}
        </div>

        {/* ── right: upcoming list ── */}
        <div className="cp-right">
          <p className="cp-section-label">Upcoming</p>
          {loading ? (
            [1,2,3].map(i => <div key={i} className="cp-skeleton" />)
          ) : upcoming.length === 0 ? (
            <div className="cp-empty">
              <span className="cp-empty-icon">📅</span>
              <p>No upcoming events</p>
            </div>
          ) : (
            upcoming.map(e => <EventCard key={e.id} event={e} onDelete={handleDelete} />)
          )}
        </div>
      </div>
    </div>
  )
}

function EventRow({ event, onDelete }) {
  return (
    <div className="cp-event-row">
      <div className="cp-event-row-info">
        <span className="cp-event-row-title">{event.title}</span>
        {event.event_time && <span className="cp-event-row-time">{event.event_time}</span>}
      </div>
      <button className="cp-icon-btn" onClick={() => onDelete(event.id)} aria-label="Delete">✕</button>
    </div>
  )
}

function EventCard({ event, onDelete }) {
  const isPast = event.event_date < fmtDate(new Date())
  const isToday = event.event_date === fmtDate(new Date())
  return (
    <div className={`cp-event-card ${isPast ? 'cp-event-card--past' : ''}`}>
      <div className="cp-event-card-date">
        <span className="cp-event-card-day">{new Date(event.event_date + 'T00:00').getDate()}</span>
        <span className="cp-event-card-month">{MONTHS[new Date(event.event_date + 'T00:00').getMonth()].slice(0,3)}</span>
        {isToday && <span className="cp-today-pill">Today</span>}
      </div>
      <div className="cp-event-card-body">
        <p className="cp-event-card-title">{event.title}</p>
        {event.event_time && <p className="cp-event-card-time">🕐 {event.event_time}</p>}
        {event.description && <p className="cp-event-card-desc">{event.description}</p>}
      </div>
      <button className="cp-icon-btn" onClick={() => onDelete(event.id)} aria-label="Delete">✕</button>
    </div>
  )
}

// helpers
function fmtDate(d) {
  return `${d.getFullYear()}-${String(d.getMonth()+1).padStart(2,'0')}-${String(d.getDate()).padStart(2,'0')}`
}

function formatDisplayDate(str) {
  const d = new Date(str + 'T00:00')
  return d.toLocaleDateString('en-US', { weekday:'long', month:'long', day:'numeric' })
}

function buildCells(year, month) {
  const first = new Date(year, month, 1).getDay()
  const days  = new Date(year, month + 1, 0).getDate()
  const cells = []
  for (let i = 0; i < first; i++) cells.push(null)
  for (let d = 1; d <= days; d++) cells.push(new Date(year, month, d))
  return cells
}
