class myclass :
    def __init__(self,x):
        self.x = x
    def prime(self):
        f = 1
        for i in range (1,self.x+1):
            f=f*i
        return f
obj = myclass(5)
f =obj.fact()
print(f)