from agent.graph import build_graph

def main():
    graph = build_graph()

    state = {
        "user_input": "",
        "intent": "",
        "response": "",
        "name": None,
        "email": None,
        "platform": None
    }

    print("🤖 AutoStream AI Agent (FREE VERSION)")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Handle lead collection BEFORE running graph
        if state["intent"] == "high_intent":
            if not state["name"]:
                state["name"] = user_input
            elif not state["email"]:
                state["email"] = user_input
            elif not state["platform"]:
                state["platform"] = user_input

        state["user_input"] = user_input

        state = graph.invoke(state)

        print("Agent:", state["response"])


if __name__ == "__main__":
    main()