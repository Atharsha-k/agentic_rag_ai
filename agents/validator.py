from config.llm import get_llm
from config.prompts import VALIDATOR_PROMPT

class ValidatorAgent:
    def __init__(self):
        self.llm = get_llm()

    def run(self, state):
        # If answer explicitly says author not mentioned, return fixed confidence
        if "do not explicitly mention the author" in state["answer"].lower():
            state["confidence"] = 0.8
            return state

        # Ask LLM to evaluate grounding
        response = self.llm.invoke(
            VALIDATOR_PROMPT.format(
                answer=state["answer"],
                context=state["context"]
            )
        )

        try:
            score = float(response.content.strip())
            # Never allow absolute certainty in RAG
            state["confidence"] = min(score, 0.9)
        except:
            state["confidence"] = 0.6

        return state
