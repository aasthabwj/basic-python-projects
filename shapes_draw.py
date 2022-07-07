import turtle
class shapes():
    def __init__(self):
        self.iut = ""
        self.z = ""
        self.a = turtle.Turtle()
    def inut(self):
        self.iut = input("ENTER A SHAPE : ")
        self.z = self.iut.lower
    def cal(self):
        if self.z == "square":
            for x in range(4):
                self.a.forward(100)
                self.a.right(90)
draw = shapes()
draw.inut()
draw.cal()
