import { useState, useRef, useEffect } from 'react'
import './ChatPage.css'

const SUGGESTIONS = [
  "What's on my task list today?",
  'Help me plan my week',
  'Set a reminder for tomorrow',
  'Summarize my priorities',
]

function ChatPage() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const bottomRef = useRef(null)
  const textareaRef = useRef(null)

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, loading])

  function autoResize() {
    const el = textareaRef.current
    if (!el) return
    el.style.height = 'auto'
    el.style.height = Math.min(el.scrollHeight, 160) + 'px'
  }

  function handleKeyDown(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      send(input)
    }
  }

  async function send(text) {
    text = text.trim()
    if (!text || loading) return

    setMessages((prev) => [...prev, { role: 'user', text }])
    setInput('')
    if (textareaRef.current) textareaRef.current.style.height = 'auto'
    setLoading(true)

    try {
      const res = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: text }),
      })
      const data = await res.json()
      setMessages((prev) => [...prev, { role: 'assistant', text: data.answer }])
    } catch {
      setMessages((prev) => [
        ...prev,
        { role: 'assistant', text: 'Could not reach the server. Is the backend running?' },
      ])
    } finally {
      setLoading(false)
    }
  }

  const isEmpty = messages.length === 0 && !loading

  return (
    <div className="chat-page">
      <div className="chat-messages">
        {isEmpty ? (
          <div className="chat-empty">
            <div className="chat-empty-icon">⚡</div>
            <div className="chat-empty-title">What can I help with?</div>
            <div className="chat-empty-sub">Your personal productivity agent is ready.</div>
            <div className="chat-suggestions">
              {SUGGESTIONS.map((s) => (
                <button key={s} className="chat-suggestion" onClick={() => send(s)}>
                  {s}
                </button>
              ))}
            </div>
          </div>
        ) : (
          <>
            {messages.map((msg, i) => (
              <div key={i} className={`chat-row chat-row--${msg.role}`}>
                <span className="chat-role-label">
                  {msg.role === 'assistant' ? 'Agent' : 'You'}
                </span>
                <div className={`chat-bubble chat-bubble--${msg.role}`}>
                  {msg.text}
                </div>
              </div>
            ))}
            {loading && (
              <div className="chat-row chat-row--assistant">
                <span className="chat-role-label">Agent</span>
                <div className="chat-bubble chat-bubble--assistant">
                  <div className="chat-typing">
                    <span /><span /><span />
                  </div>
                </div>
              </div>
            )}
          </>
        )}
        <div ref={bottomRef} />
      </div>

      <div className="chat-input-area">
        <div className="chat-input-wrap">
          <textarea
            ref={textareaRef}
            className="chat-input"
            placeholder="Message your agent..."
            value={input}
            rows={1}
            onChange={(e) => { setInput(e.target.value); autoResize() }}
            onKeyDown={handleKeyDown}
            disabled={loading}
            autoFocus
          />
          <button
            className="chat-send-btn"
            onClick={() => send(input)}
            disabled={loading || !input.trim()}
            aria-label="Send message"
          >
            ↑
          </button>
        </div>
        <p className="chat-hint">Enter to send · Shift+Enter for new line</p>
      </div>
    </div>
  )
}

export default ChatPage
