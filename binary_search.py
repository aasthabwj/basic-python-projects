number_of_elements = int(input("How many number of elements you are going to add : "))
l = list()
for y in range(0,number_of_elements):
    l.append(int(input("Enter a number : ")))
x = int(input("Input a number to search : "))
a = 0
b = number_of_elements-1
c = 0
l.sort()
print(l)
while a <= b :
    c = (a + b)//2
    if l[c] == x:
        print("Number found at ",format(c+1))
        break
    elif x > l[c]:
        a = c + 1
    else:
        b = c - 1
if a> b :
    print("Number not found.")