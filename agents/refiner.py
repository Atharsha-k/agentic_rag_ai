from config.llm import get_llm
from config.prompts import REFINER_PROMPT

class RefinerAgent:
    def __init__(self):
        self.llm = get_llm()

    def run(self, state):
        # Only refine if no context is found
        if not state.get("context"):
            response = self.llm.invoke(
                REFINER_PROMPT.format(query=state["query"])
            )
            state["query"] = response.content.strip()
        return state
