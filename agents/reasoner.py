from config.llm import get_llm
from config.prompts import REASONER_PROMPT

class ReasoningAgent:
    def __init__(self):
        self.llm = get_llm()

    def run(self, state):
        response = self.llm.invoke(
            REASONER_PROMPT.format(
                query=state["query"],
                context="\n".join(state["context"])
            )
        )
        state["answer"] = response.content
        return state
