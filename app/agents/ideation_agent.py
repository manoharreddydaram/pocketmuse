from .base import AgentResult, BaseAgent
import concurrent.futures
class IdeationAgent(BaseAgent):
    def run_parallel(self,summary,n=3):
        ideas=[]
        with concurrent.futures.ThreadPoolExecutor() as ex:
            for i in range(n): ideas.append(self.llm.generate(f"Idea seed {i}"))
        return AgentResult("ideation",ideas,{})
