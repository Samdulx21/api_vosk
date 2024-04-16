import React from "react"
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import HomePage from './pages/HomePage'
import RecognizerPage from './pages/RecognizerPage'
import ChatBotComponent from "./pages/ChatBotComponent"

function App() {
 

  return (
    <BrowserRouter>
        <Routes>
          <Route path="/" element={ <HomePage /> } />
          <Route path="/recognizer" element={ <RecognizerPage /> } />
          <Route path="/chatbot" element={ <ChatBotComponent /> } />
        </Routes>
    </BrowserRouter>
  )
}

export default App
