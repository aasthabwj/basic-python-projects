class myclass :
    def __init__(self,x):
        self.x = x
    def fact(self):
        f = 1
        for i in range (1,self.x+1):
            f=f*i
        return f
obj = myclass(4)
f =obj.fact()
print(f)