# 💬 OpenRouter Chatbot (LangGraph + LangSmith)

An intelligent chatbot built using **OpenRouter, LangGraph, LangSmith, FastAPI, and Streamlit.**
This project demonstrates how to build a traceable, modular, graph-based chatbot workflow using stateful reasoning and real-time message tracking.

# 🚀 Features
**✅ LangGraph-powered AI workflow**
+ Node-based conversational pipeline
+ Clean state transitions
+ Modular processing architecture

 **✅ OpenRouter LLM Integration**

+ Uses OpenRouter API to access powerful models
+ Currently configured with openai/gpt-4o-mini

**✅ LangSmith Observability**
+ Full tracing of requests
+ Debugging, evaluation and analytics

**✅ FastAPI Backend**
+ /chat endpoint for programmatic access
+ Lightweight and production-ready API

**✅ Streamlit Frontend**
+ Chat UI
+ Session-based chat history
+ Real-time conversation interface

# 🧠 Architecture Overview
+ User → Streamlit UI → Workflow (LangGraph)
     → input_node → ai_node → OpenRouter → reply
     → UI Response / API Response

**LangGraph Workflow**
+ input_node receives user message

+ ai_node generates reply using OpenRouter

+ Graph ends → returns final state

**LangSmith**

+ Tracks entire graph execution

+ Provides debugging and evaluation logs

📂 Project Structure
📦 openrouter-chatbot
├── main.py           # FastAPI backend
├── graph.py           # LangGraph workflow
├── agent.py           # OpenRouter message handler
├── ro.py             # Streamlit Chat UI
├── langsmith_setup.py  # LangSmith setup and environment variables
├── .env                 # API keys (not committed to GitHub)
└── requirements.txt   # Project dependencies



# 🔧 Installation & Setup
**1️⃣ Clone the repository**
git clone https://github.com/your-username/openrouter-chatbot.git
cd openrouter-chatbot

**2️⃣ Install dependencies**
+ Create a virtual environment (recommended):
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows

+ Install packages:
  pip install -r requirements.txt

**3️⃣ Set Environment Variables**
+ Create a .env file in the project root:
OPENROUTER_API_KEY=your_openrouter_api_key

LANGSMITH_API_KEY=your_langsmith_key
LANGSMITH_PROJECT=OpenRouter-Chatbot
LANGCHAIN_TRACING_V2=true

# 🔌 Running the Project
**➡ Run FastAPI Backend**
python main.py

**Your API will be available at:**

+ GET / → health check
+ POST /chat → chatbot endpoint
+ Example request:
POST /chat
{
  "message": "Hello!"
}

Response:

{
  "reply": "Hello! How can I help you today?"
}

**➡ Run Streamlit Web App**
streamlit run ro.py

**Features:**
+ Clean UI
+ Chat history
+ Real-time conversations

# 🧩 Code Explanation
**LangGraph Workflow**
+ File: graph.py 

workflow_graph = StateGraph(ChatState)
workflow_graph.add_node("input", input_node)
workflow_graph.add_node("ai", ai_node)
workflow_graph.add_edge("input", "ai")
workflow_graph.add_edge("ai", END)
workflow = workflow_graph.compile()

**Message Processing with OpenRouter**
+ File: agent.py 
response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": message}]
)

**LangSmith Initialization**
+ File: langsmith_setup.py 
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY")

# 🌐 API Endpoints
+ Health Check:
GET /

+ Response:

{"message": "OpenRouter Chatbot with LangGraph + LangSmith is running"}

+ Chat Endpoint
POST /chat

+ Payload:

{
  "message": "Your question here"
}

# 🛠 Requirements
Typical requirements.txt:
1.fastapi
2.uvicorn
3.streamlit
4.langgraph
5.langsmith
6.python-dotenv
7. openai

# 🧪 Future Enhancements
+ 🔄 Memory-enabled conversations
+ 📚 Knowledge retrieval (RAG)
+ 🔐 User authentication
+ 🚀 Docker container setup
+ 🤖 Support for multiple OpenRouter models

# 🤝 Contributing

Pull requests are welcome!
Please follow standard GitHub PR workflow.

# 📜 License

This project is licensed under the MIT License.




