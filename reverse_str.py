s = input ("Enter a sentence : ")
s=s+" "
word = ""
sent = ""
for i in range (0,len(s)):
    word = s[i] + word
    if s[i] == ' ':
        sent = sent + word
        word = ""
print(sent)