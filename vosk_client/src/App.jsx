import React from "react"
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import HomePage from './pages/HomePage'
import RecognizerPage from './pages/RecognizerPage'

function App() {
 

  return (
    <BrowserRouter>
        <Routes>
          <Route path="/" element={ <HomePage /> } />
          <Route path="/recognizer" element={ <RecognizerPage /> } />
        </Routes>
    </BrowserRouter>
  )
}

export default App
