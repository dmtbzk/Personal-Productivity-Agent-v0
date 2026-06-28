import Header from './components/Header'
import Footer from './components/Footer'
import ChatPage from './components/ChatPage'
import './App.css'

function App() {
  return (
    <div className="app-layout">
      <Header />
      <main className="app-main">
        <ChatPage />
      </main>
      <Footer />
    </div>
  )
}

export default App
