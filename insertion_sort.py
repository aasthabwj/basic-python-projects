a = int(input("How many elements are you going to add in the list : "))
l = list()
for x in range (0,a):
    l.append(int(input("Enter a number : ")))
n = len(l)
for i in range(1,n):
    key = l[i]
    j = i - 1
    while j >= 0 and l[j]>key:
        l[j+1]=l[j]
        j=j-1
    l[j+1]=key
print(l)

