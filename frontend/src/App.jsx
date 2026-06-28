import { useState } from 'react'
import Header from './components/Header'
import Footer from './components/Footer'
import ChatPage from './components/ChatPage'
import TodoPage from './components/TodoPage'
import HabitsPage from './components/HabitsPage'
import './App.css'

function App() {
  const [page, setPage] = useState('chat')

  return (
    <div className="app-layout">
      <Header page={page} onNavigate={setPage} />
      <main className="app-main">
        {page === 'chat'   && <ChatPage />}
        {page === 'tasks'  && <TodoPage />}
        {page === 'habits' && <HabitsPage />}
      </main>
      <Footer />
    </div>
  )
}

export default App
