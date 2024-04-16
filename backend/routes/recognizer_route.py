from fastapi import APIRouter
from controllers.recogn_controller import *
from controllers.recogn_controller2 import *

router = APIRouter()

model_path = r"C:\Users\userd\OneDrive\Escritorio\api_vosk\backend\model_vosk\vosk-model-small-es-0.42"
recognizer = VoskRecognizer(model_path)
recognizer_bot = SimpleChatbot(model_path)

@router.get("/recognizer")
async def recognize_speech():
    text = recognizer.record_text()
    recognizer.output_text(text)
    return {"text": text}

@router.get("/recognizer/chatbot")
async def recognize_speech():
    text = recognizer_bot.record_text()
    response = recognizer_bot.respond(text)
    print("Chatbot response:", response)
    return {"text": text, "response": response}
