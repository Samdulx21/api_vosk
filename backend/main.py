from fastapi import FastAPI
from routes import recognizer_route
from fastapi.middleware.cors import CORSMiddleware
import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return {"msg:": "FastApi"}

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    #"http://localhost"
    "http://localhost:5173"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(recognizer_route.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)