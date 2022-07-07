a = input("Type a sentence and we will display the pallindrome words in it : ")
b = ""
c = ""
d = (a+" ")
for i in range (0,len(d)):
    if d[i]==" ":
        for j in b :
            c= j+c
        if c==b:
            print(b)
        b = ""
        c = ""
    else:
        b=b+d[i]