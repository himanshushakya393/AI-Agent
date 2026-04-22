from langgraph.graph import StateGraph
from agent.state import AgentState
from agent.intent import detect_intent
from agent.rag import get_answer
from agent.tools import mock_lead_capture


def intent_node(state: AgentState):
    # Only detect intent once OR if not in lead flow
    if state["intent"] != "high_intent":
        state["intent"] = detect_intent(state["user_input"])
    return state


def response_node(state: AgentState):
    intent = state["intent"]

    if intent == "greeting":
        state["response"] = "Hi 👋 Welcome to AutoStream! Ask me about pricing or features."

    elif intent == "pricing":
        state["response"] = get_answer(state["user_input"])

    elif intent == "high_intent":
        # Step-by-step lead collection
        if not state.get("name"):
            state["response"] = "Great choice 🚀 What's your name?"
        elif not state.get("email"):
            state["response"] = "Please share your email."
        elif not state.get("platform"):
            state["response"] = "Which platform do you create content on?"
        else:
            mock_lead_capture(
                state["name"],
                state["email"],
                state["platform"]
            )
            state["response"] = "🎉 Done! Our team will contact you soon."

    else:
        state["response"] = "I can help with pricing or getting started!"

    return state


def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("intent", intent_node)
    builder.add_node("response", response_node)

    builder.set_entry_point("intent")
    builder.add_edge("intent", "response")

    return builder.compile()