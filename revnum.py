def rdi(a,s):
    if(a==0):
       return s
    else:
        b = a % 10
        a = a//10
        s = s*10 + b
        return rdi(a,s)


a = int(input("WRITE A NUMBER TO FIND ITS REVERSE : "))
print(rdi(a,0))
