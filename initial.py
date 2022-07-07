a = input("Enter a name and we will give its initials : ")
b = ""
for x in range(0,len(a)) :
    if a[x]==" ":
        b = b+a[x+1] + ". "
print (a[0],".",b)

