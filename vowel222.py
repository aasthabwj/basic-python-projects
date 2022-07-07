class kuchbhi :
    def __init__(self):
        self.st = ""
        self.y = 0
    def inup(self):
        self.st = input("Input a sentence : ")
    def vowel(self):
        for x in range(0,len(self.st)-1):
            if self.st[x] in ("a","e","i","o","u"):
                self.y = self.y+1
        print(self.y)
v2 = kuchbhi()
v2.inup()
v2.vowel()
                
