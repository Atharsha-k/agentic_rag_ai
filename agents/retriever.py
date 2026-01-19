from config.llm import get_llm
class RetrieverAgent:
    def __init__(self, store, embedder):
        self.store = store
        self.embedder = embedder

    def run(self, state):
        emb = self.embedder.embed([state["query"]])[0]
        state["context"] = self.store.search(emb)
        return state
