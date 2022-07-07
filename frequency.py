str=input('Write a sentence: ')
d1 = {}
num = 0
words = str.split()
for x in words:
    if x not in d1:
        d1[x] = 1
    else:
        d1[x] +=1
print(d1)
