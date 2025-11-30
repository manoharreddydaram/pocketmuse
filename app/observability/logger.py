import time, json
class Logger:
    def __init__(self, path="logs/pocketmuse.log"):
        self.path = path
    def log(self, event, data=None):
        entry={"ts":time.time(),"event":event,"data":data or {}}
        print("LOG>", entry)
        f=open(self.path,"a"); f.write(json.dumps(entry)+"\n"); f.close()
