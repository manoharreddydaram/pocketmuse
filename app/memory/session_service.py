class InMemorySessionService:
    def __init__(self): self.sessions={}
    def create_session(self,id,data=None): self.sessions[id]=data or {}
    def get(self,id): return self.sessions.get(id,{})
