class std :
    def __init__(self):
        self.nm = 0
        self.rn = ""
        self.ads = ""
    def ind(self):
        self.nm = input("NAME : ")
        self.rn = int(input("ROLL NO. : "))
        self.ads = input("ADRESS : ")
    def showdata(self):
        print(self.nm,self.rn,self.ads)
student = std()
student.ind()
student.showdata()
