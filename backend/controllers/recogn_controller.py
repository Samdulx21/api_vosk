from vosk import Model, KaldiRecognizer
from config.database import get_db_connection
from models.recogn_model import RecognText
import pyaudio
import json
import mysql.connector

class VoskRecognizer:
    def __init__(self, model_path):
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)
        self.mydb = get_db_connection()

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
                    if 'text' in result:
                        recognized_text = result['text']
                        print("Reconocido:", recognized_text)
                        return recognized_text

            final_result = json.loads(self.recognizer.FinalResult())
            if 'text' in final_result:
                recognized_text = final_result['text']
                print("Reconocido:", recognized_text)
                return recognized_text

        except Exception as e:
            print("Error:", e)

    def output_text(self, text: str):
        try:
            self.db = self.mydb.cursor() 
            sql = "INSERT INTO avrecogn_text(recogn_text) VALUES(%s)"
            new_text = text
            self.db.execute(sql, (new_text,))
            self.mydb.commit()
            self.db.close()
            with open("output.txt", "a") as f:
                f.write(text + "\n")
        except mysql.connector.Error as err:
            self.mydb.rollback()
            print("Error en la base de datos:", err)
        except Exception as e:
            print("Error desconocido:", e)


    def continuous_recognition(self):
        while True:
            text = self.record_text()
            if text:
                recogn_text = RecognText(text)
                self.output_text(text, recogn_text)
                print("Texto escrito en archivo")

# Uso de la clase VoskRecognizer
if __name__ == "__main__":
    model_path = r"C:\Users\DEV JUNIOR\Documents\api_vosk\backend\model_vosk\vosk-model-small-es-0.42"
    recognizer = VoskRecognizer(model_path)
    recognizer.continuous_recognition()
