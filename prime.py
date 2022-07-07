a = int(input("WRITE A NUMBER TO FIND IT IS PRIME OR NOT : "))
b = 0
for x in range (1,a+1):
    if a%x == 0 :
        b = b+1
if b>2:
    print("IT IS A NOT PRIME NUMBER.")
else:
     print("IT IS A PRIME NUMBER.")