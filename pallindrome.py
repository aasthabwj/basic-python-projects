a = int(input("WRITE A NUMBER TO FIND WHETHER IT IS A PALLINDROME : "))
c=0
x = a
while (a>0):
    b = a % 10
    a = a//10
    c = 10*c+b
if c == x:
    print ("IT IS A PALLINDROME.")
else:
    print("IT IS NOT A PALLINDROME.")