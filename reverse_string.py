def rev(l,x):
    if x < 0:
        return
    print(l[x],end="")
    rev(l,x-1)


l = input("ENTER ANYTHING :")
rev(l,len(l)-1)
