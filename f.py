number = [5,5,5,2,2,2,2,2,2,2,5,5,5,2,2,2,2,2,2,2,2,2]
for x in number:
    print(x*"000000")
print('''





''')
for y in number:
    output = ""
    for z in range(y):
        output +="000000"
    print(output)
