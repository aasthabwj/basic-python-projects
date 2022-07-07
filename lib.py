class library():
    def __init__(self):
        self.acn = 0
        self.tle = ""
        self.aut = ""
        self.das = 0
        self.mon = 0
    def iut(self):
        self.acn = int(input("WRITE ACCESSION NUMBER : "))
        self.tle = input("WRITE THE TITLE OF THE BOOK : ")
        self.aut = input("WRITE THE NAME OF THE AUTHOR : ")
    def comp(self):
        self.das = int(input("WRITE THE NUMBER OF DAYS FOR WHICH YOU BORROWED THE BOOK : "))
        self.mon = self.das*2
    def display(self):
        print("ACCESSION NUMBER     :     ",self.acn)
        print("AUTHOR               :     ", self.aut.upper())
        print("TITLE                :     ",self.tle.upper())
        print("PAYMENT              :     ", self.mon,"$")
lib = library()
lib.iut()
lib.comp()
lib.display()