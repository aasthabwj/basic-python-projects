def disu(a):
    s = 0
    if(a==0):
       return 0
    else:
        b = a % 10
        s = b + disu(a//10)
        return s

a = int(input("WRITE A NUMBER TO FIND SUM OF ITS DIGITS : "))
print(disu(a))