class est:
    def __init__(self):
        self.nm = ""
        self.wt = 0
        self.ch = 0
    def acc(self):
        self.nm = input("Insert your name : ")
        self.wt = int(input("Insert weight in kg : "))
    def calc(self):
        if self.wt <= 10:
            self.ch = self.wt*25
        elif self.wt > 10 and self.wt <= 30:
            self.ch = ((self.wt-10)*20)+250
        elif self.wt > 30:
            self.ch = ((self.wt-30)*10)+650
        self.ch = self.ch + self.ch*0.05
    def dis(self):
        print("NAME    : ",self.nm)
        print("WEIGHT  : ",self.wt)
        print("PAY     : ",self.ch)
estimate = est()
estimate.acc()
estimate.calc()
estimate.dis()
