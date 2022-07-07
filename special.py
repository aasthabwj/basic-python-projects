class spc:
    def __init__(self):
        self.li = list()
        self.n = None
    def inp(self):
        self.n = int(input("ENTER THE SIZE : "))
        for x in range(1,self.n+1):
            self.li.append(int(input("ENTER A NUMBER : ")))
    def factorial(self,a):
        if a == 1:
            return 1
        else:
            s = a * self.factorial(a - 1)
            return s
    def check(self):
        for y in (self.li):
            x = y
            s=0
            while x>0 :
                i = x%10
                j = self.factorial(i)
                x =x//10
                s = s + j
            if s == y:
                print(y," is a special number.")
            else:
                print(y, " is not a special number.")
sd = spc()
sd.inp()
sd.check()