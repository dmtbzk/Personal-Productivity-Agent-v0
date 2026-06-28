import './Header.css'

function Header({ page, onNavigate }) {
  return (
    <header className="header">
      <div className="header-inner">
        <div className="header-brand">
          <div className="header-icon" aria-hidden="true">⚡</div>
          <div>
            <div className="header-title">Productivity Agent</div>
            <div className="header-subtitle">by Demet Bozkurt</div>
          </div>
        </div>

        <nav className="header-nav">
          {[
            { key: 'chat',   label: '💬 Chat' },
            { key: 'tasks',  label: '✓ Tasks' },
            { key: 'habits',   label: '🌱 Habits' },
            { key: 'calendar', label: '📅 Calendar' },
          ].map(({ key, label }) => (
            <button
              key={key}
              className={`header-nav-btn ${page === key ? 'header-nav-btn--active' : ''}`}
              onClick={() => onNavigate(key)}
            >
              {label}
            </button>
          ))}
        </nav>

        <div className="header-status">
          <span className="status-dot" aria-hidden="true" />
          Online
        </div>
      </div>
    </header>
  )
}

export default Header
