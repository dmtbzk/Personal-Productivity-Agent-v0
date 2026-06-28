import './Header.css'

function Header() {
  return (
    <header className="header">
      <div className="header-inner">
        <div className="header-logo">
          <span className="header-logo-icon">🤖</span>
          <span className="header-logo-text">Productivity Agent</span>
        </div>
        <nav className="header-nav">
          <a href="#">Chat</a>
          <a href="#">Tasks</a>
        </nav>
      </div>
    </header>
  )
}

export default Header
