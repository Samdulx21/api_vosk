from vosk import Model, KaldiRecognizer
import pyaudio
import json

class SimpleChatbot:
    def __init__(self, model_path):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.responses = {
            "hola": "¡Hola! ¿En qué puedo ayudarte?",
            "cómo estás": "Estoy bien, gracias por preguntar.",
            "adiós": "¡Hasta luego!",
            "qué haces": "Estoy aquí para ayudarte.",
            "quién eres": "Soy un chatbot creado para ayudarte con consultas simples.",
            "cuál es tu nombre": "Puedes llamarme Chatbot."
        }

    def record_text(self):
        try:
            mic = pyaudio.PyAudio()
            stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=2048)
            stream.start_stream()

            while True:
                data = stream.read(2048)
                if len(data) == 0:
                    break
                if self.recognizer.AcceptWaveform(data):
                    result = json.loads(self.recognizer.Result())
                    if result['text']:
                        return result['text']

            result = json.loads(self.recognizer.FinalResult())
            if result['text']:
                return result['text']

        except Exception as e:
            print("Error:", e)

    def respond(self, text):
        text = text.lower()
        if text in self.responses:
            return self.responses[text]
        else:
            return "Lo siento, no entendí eso."