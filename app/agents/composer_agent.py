from .base import AgentResult, BaseAgent
class ComposerAgent(BaseAgent):
    def run(self,idea,val,memory):
        return AgentResult("composer",self.llm.generate(f"compose {idea}"),{})
