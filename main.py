from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import run_agent

app = FastAPI()

# Allow Streamlit frontend to access this
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, use the real frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(payload: dict):
    user_input = payload.get("user_input")
    print(f"🟡 Received input: {user_input}")
    try:
        response = await run_agent(user_input)
        print(f"🟢 Agent response: {response}")
        return {"response": response}
    except Exception as e:
        print(f"🔴 Error: {e}")
        return {"response": "Sorry, I couldn't respond."}

