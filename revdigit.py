def rdi(a):
    if(a==0):
       return
    else:
        b = a % 10
        print(b,end="")
        rdi(a//10)


a = int(input("WRITE A NUMBER TO FIND ITS REVERSE : "))
rdi(a)