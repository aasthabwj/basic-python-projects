class dat:
    def __init__(self):
        self.day = 0
        self.mon = 0
        self.yea = 0
    def iut(self):
        self.day = int(input("ENTER THE DAY   : "))
        self.mon = int(input("ENTER THE MONTH : "))
        self.yea = int(input("ENTER THE YEAR  : "))
        if self.day > 30 or self.day < 1 or self.mon > 12 or self.mon < 1:
            print("wrong")
            return False
        else:
            return True
    def __sub__(self,a):
        d1 = dat()
        d1.day = self.day - a.day
        d1.mon = self.mon - a.mon
        d1.yea = self.yea - a.yea
        if d1.day <= 0 :
            d1.mon = d1.mon - 1
            d1.day = d1.day + 30
        if d1.mon <= 0:
            d1.mon = d1.mon + 12
            d1.yea = d1.yea - 1
        return d1
    def pri(self):
        print(self.day,"-",self.mon,"-",self.yea)
d2 = dat()
if d2.iut() == False:
    exit()
d3 = dat()
if d3.iut() == False:
    exit()
d4 = d2 - d3
d4.pri()