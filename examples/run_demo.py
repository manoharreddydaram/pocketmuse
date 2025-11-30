from app.llm_client import LLMClient
from app.observability.logger import Logger
from app.agents.research_agent import ResearchAgent
from app.agents.ideation_agent import IdeationAgent
from app.agents.validator_agent import ValidatorAgent
from app.agents.composer_agent import ComposerAgent
from app.memory.memory_bank import MemoryBank
llm=LLMClient();logger=Logger();mem=MemoryBank()
r=ResearchAgent(llm,logger).run("ai apps")
i=IdeationAgent(llm,logger).run_parallel(r.output)
v=ValidatorAgent(llm,logger).run(i.output[0])
c=ComposerAgent(llm,logger).run(i.output[0],v.output,mem)
print(c.output)
