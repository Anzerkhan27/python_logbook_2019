"""
Confirming a password entered by a User

"""


password = input("Enter password: ")
if len(password) in range(6,13):
    check = input("re enter password: ")
    if password == check:
        print("password changed")
    else:
        print("password didn't match!")
else:
    print("Password must be 6 to 12 characters!")
