from fastapi import FastAPI
from graph import workflow
from langsmith_setup import setup_langsmith
import uvicorn

setup_langsmith()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "OpenRouter Chatbot with LangGraph + LangSmith is running"}

@app.post("/chat")
def chat(data: dict):
    user_msg = data.get("message", "")
    result = workflow.invoke({"message": user_msg})
    return {"reply": result["reply"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
