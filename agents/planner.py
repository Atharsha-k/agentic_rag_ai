from config.llm import get_llm
from config.prompts import PLANNER_PROMPT

class PlannerAgent:
    def __init__(self):
        self.llm = get_llm()

    def run(self, state):
        response = self.llm.invoke(
            PLANNER_PROMPT + "\nQuery:\n" + state["query"]
        )
        state["action"] = response.content.strip().lower()
        return state
