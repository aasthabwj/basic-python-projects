class person:
    def __init__(self,fn,ln):
        self.fnm = fn
        self.lnm = ln
    def pn(self):
        print(self.fnm,self.lnm)
x = person("John","Doe")
x.pn()
class student(person):
    def __init__(self,fn,ln,ftn,mtn):
        self.frn = ftn
        self.lsn = mtn
        self.fnm = fn
        self.lnm = ln
    def dpl(self):
        print(self.frn,self.lsn)
y = student("Don","Joe","Pro","Darsh")
y.pn()
y.dpl()