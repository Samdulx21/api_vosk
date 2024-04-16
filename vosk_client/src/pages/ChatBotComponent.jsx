import React, { useState } from 'react';

function App() {
  const [recognizedText, setRecognizedText] = useState('');
  const [responseText, setResponseText] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const recognizeSpeech = async () => {
    setIsLoading(true);
    try {
      const response = await fetch('http://localhost:8000/recognizer/chatbot');
      const data = await response.json();
      setRecognizedText(data.text);
      setResponseText(data.response);
    } catch (error) {
      console.error('Error:', error);
      setRecognizedText('Error al comunicarse con el servidor');
    }
    setIsLoading(false);
  };

  return (
    <div>
      <h1>Reconocimiento de Voz</h1>
      <button onClick={recognizeSpeech} disabled={isLoading}>
        {isLoading ? 'Cargando...' : 'Comenzar Reconocimiento'}
      </button>
      <div>
        {recognizedText && (
          <div>
            <h2>Texto Reconocido:</h2>
            <p>{recognizedText}</p>
          </div>
        )}
      </div>
        <div className='py-4'>
        {responseText && (
          <div>
            <h2>Respuesta del bot:</h2>
            <p>{responseText}</p>
          </div>
        )}
        </div>

    </div>
  );
}

export default App;