s = input ("Enter a sentence : ")
s=s+" "
word = ""
sent = ""
for i in range (0,len(s)):
    word = word + s[i]
    if s[i] == ' ':
        sent = word + sent
        word = ""
print(sent)