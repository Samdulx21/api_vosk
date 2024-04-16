from pydantic import BaseModel

class ChatbotModel(BaseModel):
    recogn_chat: str
    bot_respond: str


class SayColor(BaseModel):
    color: str


class RecognText(BaseModel):
    r_text: str

