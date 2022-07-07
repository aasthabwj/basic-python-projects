a = int(input("WRITE FIRST NUMBER : "))
b = int(input("WRITE SECOND NUMBER : "))
x = min(a,b)
y = max(a,b)
while (x>0):
    y = y//x
    x = y%x
print(y)