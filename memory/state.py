from typing import TypedDict, List

class AgentState(TypedDict):
    query: str
    action: str
    context: List[str]
    answer: str
    confidence: float
