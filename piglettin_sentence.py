a = input("Enter a sentence : ")
a=a+" "
b = ""
c = ""
for x in range (0,len(a)):
     if a[x]==" ":
        for j in range (0,len(b)) :
            if b[j] == "a" or b[j] == "e" or b[j] == "i" or b[j] == "o" or b[j] == "u":
                c = c+ " " + b[j:] + b[:j] + "ay"
                b=""
                break
     else :
         b= b+a[x]
print(c)
