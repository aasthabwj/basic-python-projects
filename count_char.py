def countchar(str1,ch):
    count = 0
    for s in str1:
        if s == ch :
            count+=1
    return count
msg = input("Enter any string : ")
ch = input("Enter character to count in string : ")
c = countchar(msg,ch)
if c==0:
    print("Sorry!",ch,"is not in ",msg)
else:
    print(ch," found", c , "times in ",msg)
