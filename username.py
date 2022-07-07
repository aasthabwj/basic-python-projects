usid = input("Write your ID: ")
usp = input("Write your password: ")
def check_pwd():
    if usid == "darsh" and usp == "bhilwara":
        print("LOGIN SUCCESSFUL.")
    else:
        print("INVALID ID OR PASSWORD.")
check_pwd()
