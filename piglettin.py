a = input("Enter a word : ")
b = 0
for x in range (0,len(a)):
    if a[x] =="a" or a[x]=="e" or a[x]=="i" or a[x]=="o" or a[x]=="u":
        b =a[x:]+a[:x]+"ay"
        break
print(b)
