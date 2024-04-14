from fastapi import APIRouter
from controllers.recogn_controller import *



router = APIRouter()

model_path = r"C:\Users\Millow\Desktop\api_vosk\backend\model_vosk\vosk-model-small-es-0.42"
recognizer = VoskRecognizer(model_path)

@router.get("/recognizer")
async def recognize_speech():
    text = recognizer.record_text()
    recognizer.output_text(text)
    return {"text": text}
