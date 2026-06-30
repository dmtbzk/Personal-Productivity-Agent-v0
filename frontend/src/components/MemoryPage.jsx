import { useState, useEffect } from 'react'
import { fetchMemory, deleteMemory } from '../api'
import './MemoryPage.css'

const CATEGORY_ICONS = {
  profile:    '👤',
  routine:    '⏰',
  preference: '⭐',
  goal:       '🎯',
  default:    '🧠',
}

const CATEGORY_COLORS = {
  profile:    'blue',
  routine:    'amber',
  preference: 'purple',
  goal:       'green',
  default:    'gray',
}

export default function MemoryPage() {
  const [items, setItems]     = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError]     = useState(null)
  const [search, setSearch]   = useState('')

  useEffect(() => { load() }, [])

  async function load() {
    try {
      setLoading(true); setError(null)
      setItems(await fetchMemory())
    } catch {
      setError('Could not load memory. Is the backend running?')
    } finally {
      setLoading(false)
    }
  }

  async function handleDelete(id) {
    setItems(prev => prev.filter(m => m.id !== id))
    try { await deleteMemory(id) } catch { load() }
  }

  const filtered = items.filter(m => {
    const q = search.toLowerCase()
    return !q || m.key.includes(q) || m.value.toLowerCase().includes(q) || m.category.includes(q)
  })

  // group by category
  const groups = filtered.reduce((acc, m) => {
    acc[m.category] = acc[m.category] || []
    acc[m.category].push(m)
    return acc
  }, {})

  return (
    <div className="mp-page">
      <div className="mp-header">
        <div>
          <h1 className="mp-title">Memory</h1>
          <p className="mp-sub">What your agent knows about you.</p>
        </div>
        <button className="mp-refresh" onClick={load} title="Refresh">↻</button>
      </div>

      {error && <div className="mp-error">{error}</div>}

      {!loading && items.length > 0 && (
        <div className="mp-search-wrap">
          <span className="mp-search-icon">🔍</span>
          <input
            className="mp-search"
            type="text"
            placeholder="Search memory..."
            value={search}
            onChange={e => setSearch(e.target.value)}
          />
          {search && (
            <button className="mp-search-clear" onClick={() => setSearch('')}>✕</button>
          )}
        </div>
      )}

      {loading ? (
        <div className="mp-groups">
          {[1, 2, 3].map(i => <div key={i} className="mp-skeleton" />)}
        </div>
      ) : items.length === 0 ? (
        <div className="mp-empty">
          <div className="mp-empty-icon">🧠</div>
          <p className="mp-empty-title">No memories yet</p>
          <p className="mp-empty-sub">Tell the agent something to remember via Chat.</p>
        </div>
      ) : filtered.length === 0 ? (
        <div className="mp-empty">
          <div className="mp-empty-icon">🔍</div>
          <p className="mp-empty-title">No results</p>
          <p className="mp-empty-sub">Try a different search term.</p>
        </div>
      ) : (
        <div className="mp-groups">
          {Object.entries(groups).map(([category, memories]) => (
            <div key={category} className="mp-group">
              <div className="mp-group-head">
                <span className="mp-group-icon">
                  {CATEGORY_ICONS[category] || CATEGORY_ICONS.default}
                </span>
                <span className={`mp-group-label mp-group-label--${CATEGORY_COLORS[category] || 'gray'}`}>
                  {category}
                </span>
                <span className="mp-group-count">{memories.length}</span>
              </div>
              <div className="mp-group-body">
                {memories.map(m => (
                  <MemoryRow key={m.id} item={m} onDelete={handleDelete} />
                ))}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  )
}

function MemoryRow({ item, onDelete }) {
  return (
    <div className="mp-row">
      <div className="mp-row-content">
        <span className="mp-row-key">{item.key.replace(/_/g, ' ')}</span>
        <span className="mp-row-value">{item.value}</span>
      </div>
      <span className="mp-row-date">{formatDate(item.updated_at)}</span>
      <button
        className="mp-delete"
        onClick={() => onDelete(item.id)}
        aria-label="Forget this"
      >✕</button>
    </div>
  )
}

function formatDate(str) {
  return new Date(str).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })
}
