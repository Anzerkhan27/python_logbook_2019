"""
Confirming a password entered by a User
Password should not  contain, Username, student id,"huddersfield","justin beiber", "cheese", "canalside"

"""


username = input("Enter username: ")
student_id =  input("Enter student id: ")

password = input("Enter password: ")
if len(password) in range(6,13) :
    if (password) in [(username),(student_id), "huddersfield","justin beiber", "cheese", "canalside"]:
        print("password must not conatin {} , {} , 'huddersfield','justin bieber','cheese','canalside'".format(username,student_id))
    else:
        check = input("re enter password: ")
        if password == check:
            print("password changed")
        else:
            print("password didnt match!")


else:
    print("Password must be 6 to 12 characters!")