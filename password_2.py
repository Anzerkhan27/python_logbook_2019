"""
Confirming a password entered by a User(Improved Version)
Password should not  contain, Username, student id,"huddersfield","justin beiber", "cheese", "canalside"

"""


username = input("Enter username: ")
student_id =  input("Enter student id: ")
while True:
    password = input("Enter password: ")

    if len(password) in range(6,13) :
        if str(password) in [str(username),str(student_id), "huddersfield","password", "cheese", "programming"]:
            print("password must not conatin {} , {} , 'huddersfield','justin bieber','cheese','programming'".format(username,student_id))
        else:
            check = input("re enter password: ")
            if password == check:
                print("password changed")
                break
            else:
                print("password didnt match!")


    else:
        print("Password must be 6 to 12 characters!")