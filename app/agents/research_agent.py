from .base import AgentResult, BaseAgent
from ..tools.web_search import web_search
class ResearchAgent(BaseAgent):
    def run(self,topic):
        self.logger.log("research.start",{"topic":topic})
        refs=web_search(topic)
        summary=self.llm.generate(f"Research: {topic}")
        return AgentResult("research",summary,{"refs":refs})
