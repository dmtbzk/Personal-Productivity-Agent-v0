import './Footer.css'

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-inner">
        <span>© {new Date().getFullYear()} Productivity Agent</span>
        <span className="footer-sep">·</span>
        <span>All conversations are private</span>
      </div>
    </footer>
  )
}

export default Footer
