b = int(input("WRITE A NUMBER TO RANGE : "))
a =  int(input("WRITE ONE MORE NUMBER TO RANGE : "))
i = min(a,b)
j = max(a,b)
for x in range (i,(j+1)):
    if x % 2 == 0 :
        print (x)
