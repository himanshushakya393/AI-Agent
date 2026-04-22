This project uses LangGraph to build a structured conversational AI agent with clear state transitions. LangGraph was chosen over standard LangChain because it provides better control over multi-step workflows like intent detection, RAG retrieval, and tool execution.

The agent maintains a shared state (AgentState) that persists across conversation turns, enabling context-aware interactions such as collecting user details step-by-step. The workflow begins with intent classification, followed by conditional branching:

Pricing queries trigger the RAG pipeline
High-intent users trigger a lead collection flow

The RAG system uses a local JSON knowledge base to ensure deterministic and fast responses without relying on external APIs.

Tool execution is handled safely — the mock_lead_capture function is only called once all required fields (name, email, platform) are collected, preventing premature execution.

This modular design ensures scalability and makes it easy to integrate additional tools or extend conversation logic.
