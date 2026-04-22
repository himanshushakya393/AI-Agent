from typing import TypedDict, Optional

class AgentState(TypedDict):
    user_input: str
    intent: str
    response: str
    name: Optional[str]
    email: Optional[str]
    platform: Optional[str]