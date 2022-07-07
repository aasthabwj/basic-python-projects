z = int(input("How many number of elements you are going to add : "))
s = list()
for y in range(0,z):
    s.append(int(input("Enter a number : ")))
word = int(input("Enter the number whose frequency you need to check : "))
l = 0
for x in s:
    if x == word:
        l += 1
print(l)