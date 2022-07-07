a = int(input("How many elements are you going to add in the list : "))
l = list()
for x in range (0,a):
    l.append(int(input("Enter a number : ")))
lth = len(l)
for y in range (lth):
    for z in range (lth):
        if l[y] < l[z]:
           l[z],l[y+1]= l[y+1],l[z]
print(l)