def change(myd,key,name):
    myd[key]=name


student = {'roll':1,'name':'amit','per':89}
print(student)
print("1. change roll" )
print("2. change name")
print("3. change percentage")
choice = int(input("Enter your choice : "))
key = None
if choice==1:
    r = int(input("Enter new rn : "))
    key='roll'
elif choice==2:
    r = (input("Enter new name : "))
    key = 'name'
elif choice==3:
    r = int(input("Enter new rn : "))
    key = 'per'
else:
    print("Invalid Choice")
if key!=None:
    change(student,key,r)
print(student)
