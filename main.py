from loaders.loader import load_documents
from embeddings.embedder import Embedder
from vectorstore.faiss_store import FAISSStore
from analysis.graph import build_graph

from agents.planner import PlannerAgent
from agents.retriever import RetrieverAgent
from agents.refiner import RefinerAgent
from agents.reasoner import ReasoningAgent
from agents.validator import ValidatorAgent
from ui.cli import ask

# Load documents
docs = load_documents("data/raw")

embedder = Embedder()
store = FAISSStore()
store.add(embedder.embed(docs), docs)

agents = {
    "planner": PlannerAgent(),
    "retriever": RetrieverAgent(store, embedder),
    "refiner": RefinerAgent(),
    "reasoner": ReasoningAgent(),
    "validator": ValidatorAgent()
}

graph = build_graph(agents)

query = ask()
state = {"query": query}

result = graph.invoke(state)

print("\nAnswer:\n", result["answer"])
print("\nConfidence:", result["confidence"])
