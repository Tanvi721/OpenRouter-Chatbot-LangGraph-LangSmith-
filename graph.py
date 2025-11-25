from langgraph.graph import StateGraph, END
from agent import process_user_message

# State definition (optional but recommended)
class ChatState(dict):
    message: str
    reply: str | None

def input_node(state: ChatState):
    return {"message": state["message"]}

def ai_node(state: ChatState):
    reply = process_user_message(state["message"])
    return {"reply": reply}

# Build graph using StateGraph
workflow_graph = StateGraph(ChatState)

workflow_graph.add_node("input", input_node)
workflow_graph.add_node("ai", ai_node)

workflow_graph.add_edge("input", "ai")
workflow_graph.add_edge("ai", END)

workflow_graph.set_entry_point("input")

workflow = workflow_graph.compile()
