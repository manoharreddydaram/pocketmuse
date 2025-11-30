import json, os
class MemoryBank:
    def __init__(self,path="data_memory.json"):
        self.path=path
        if not os.path.exists(path): open(path,"w").write("{}")
    def load(self): return json.load(open(self.path))
    def save(self,d): open(self.path,"w").write(json.dumps(d,indent=2))
