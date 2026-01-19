from langgraph.graph import StateGraph
from memory.state import AgentState

def build_graph(agents):
    graph = StateGraph(AgentState)

    graph.add_node("planner", agents["planner"].run)
    graph.add_node("retriever", agents["retriever"].run)
    graph.add_node("refiner", agents["refiner"].run)
    graph.add_node("reasoner", agents["reasoner"].run)
    graph.add_node("validator", agents["validator"].run)

    graph.set_entry_point("planner")
    graph.add_edge("planner", "retriever")
    graph.add_edge("retriever", "refiner")
    graph.add_edge("refiner", "reasoner")
    graph.add_edge("reasoner", "validator")

    return graph.compile()
