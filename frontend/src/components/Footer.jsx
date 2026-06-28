import './Footer.css'

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-inner">
        <span>© {new Date().getFullYear()} Productivity Agent</span>
        <span>Powered by FastAPI + Claude</span>
      </div>
    </footer>
  )
}

export default Footer
