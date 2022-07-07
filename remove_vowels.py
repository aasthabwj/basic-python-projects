a = input("Type a sentence and we will display it without vowels : ")
vowels = ("a","e","i","o","u")
for x in a.lower():
    if x in vowels:
        a=a.replace(x,"")
print(a)