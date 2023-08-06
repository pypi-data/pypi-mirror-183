import time

class client:
  def __init__(self,**kwargs):
    try:self.prid=kwargs['prid']
    except:self.prid=""
    
    try:self.tm=int(kwargs['tm'])
    except:self.tm=0.5
    self.clid=0
  
  def get(self):
    time.sleep(self.tm)
    with open("df.txt") as df:
      cv=df.read().split("\n")
    ccid=self.clid
    evnts = []
    for ln in cv:  
      if ln=="":continue
      cvs = ln.split(":")
      cid =int(cvs[0])
      if cid>self.clid:
        if cid>ccid:
          ccid=cid
        cmg = cvs[1]
        cda = cvs[2]
        cfor = cvs[3]
        if cfor == ".ALL" or cfor == self.prid:
          evnts.append([cmg,cda])
    self.clid=ccid 
    return evnts
  
  def clear(self):
    with open("df.txt","w")as cf2:
      cf2.write("")

class server:
    def __init__(self):
      pass
    def send(self,msg,data,for_=".ALL"):
      id = int(time.time())
      l = f"{id}:{msg}:{data}:{for_}\n"
    
      with open("df.txt","a") as df:
        df.write(l)
        df.flush()