a = input("Phone Number : ")
b = len(a)
dict = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
    "0" : "Zero"
}
char = ""
if b>10 or b<10:
    print("You think you can fool this program!!!!!!")
else:
    for x in a:
        char = char + dict.get(x) + " "
    print(char)