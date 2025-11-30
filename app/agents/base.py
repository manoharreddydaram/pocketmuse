from dataclasses import dataclass
@dataclass
class AgentResult:
    name: str
    output: any
    metadata: dict
class BaseAgent:
    def __init__(self,llm,logger): self.llm=llm; self.logger=logger
