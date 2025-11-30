# app/agents/validator_agent.py
from .base import AgentResult, BaseAgent
import json
import re

class ValidatorAgent(BaseAgent):
    def run(self, idea_text: str):
        self.logger.log("validate.start")
        prompt = ("Score this idea as JSON with keys novelty, feasibility, days_estimate "
                  "(integers 0-10 for scores, days as integer). Return only JSON.\n\n"
                  f"Idea:\n{idea_text}")
        resp = self.llm.generate(prompt)
        # try to extract JSON substring (safe)
        m = re.search(r'\{.*\}', resp, re.S)
        if m:
            try:
                data = json.loads(m.group(0))
            except Exception:
                data = {"novelty": None, "feasibility": None, "days_estimate": None, "raw": resp}
        else:
            data = {"novelty": None, "feasibility": None, "days_estimate": None, "raw": resp}
        self.logger.log("validate.finish", {"score": data})
        return AgentResult(name="validator", output=data, metadata={})
