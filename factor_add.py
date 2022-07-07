a = (int(input("ENTER A NUMBER TO FIND AND ADD ITS FACTORS : ")))
b = 0
for x in range (2,a):
    if a%x == 0 :
        b = (b+x)
print(b)