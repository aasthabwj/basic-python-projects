def my(l,x):
    if x < 0:
        return
    print(l[x])
    my(l,x-1)


l = [13,35,426,665,86,77]
my(l,len(l)-1)