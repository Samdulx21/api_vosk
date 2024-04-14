from vosk import Model, KaldiRecognizer
import pyaudio
import json

class VoskRecognizer:
    def __init__(self, model_path):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)

    def record_text(self):
        try:
            print("Escuchando...")
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
                        print("Reconocido:", result['text'])
                        return result['text']

            result = json.loads(self.recognizer.FinalResult())
            if result['text']:
                print("Reconocido:", result['text'])
                return result['text']

        except Exception as e:
            print("Error:", e)

    def output_text(self, text):
        with open("output.txt", "a") as f:
            f.write(text + "\n")

    def continuous_recognition(self):
        while True:
            text = self.record_text()
            self.output_text(text)
            print("Texto escrito en archivo")
            if text.lower() == "salir":  
                print("Saliendo del programa...")
                break  

# Uso de la clase VoskRecognizer
if __name__ == "__main__":
    model_path = r"C:\Users\Millow\Desktop\API_VOSK\backend\Jarvi\vosk-model-small-es-0.42"
    recognizer = VoskRecognizer(model_path)
    recognizer.continuous_recognition()
