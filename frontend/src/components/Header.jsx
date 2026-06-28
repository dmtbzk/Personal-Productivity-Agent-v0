import './Header.css'

function Header() {
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
        <div className="header-status">
          <span className="status-dot" aria-hidden="true" />
          Online
        </div>
      </div>
    </header>
  )
}

export default Header
