def avgsum(a):
    s = 0
    b = len(a)
    for x in a:
        s=s+x
    av = s/b
    toop = (s,av)
    return(toop)
d = []
n1 = int(input("Enter first number  : "))
n2 = int(input("Enter second number : "))
d.append(n1)
d.append(n2)
print(avgsum(d))