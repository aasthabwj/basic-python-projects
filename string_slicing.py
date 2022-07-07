a = str(input("ENTER A WORD : "))
v = 0
c = 0
s = 0
d = 0
modi = 0
for i in a:
    if i.isalpha():
        if i in ("a" , "e" , "i","o","u"):
            v = v+1
        else :
            c = c+1
    elif i.isdigit():
        d = d+1
    elif (i == " "):
        s = s+1
    else :
        modi = modi+1

print(c)
print(modi)
print(v)
print(s)
print(d)