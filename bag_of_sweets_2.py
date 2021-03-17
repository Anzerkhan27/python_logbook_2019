"""
  Modified Version  for Diving the total number of Sweets among total number of students
  The remaining sweets are given to the teacher
  User can enter the total number of students and sweets

"""

Number_of_sweets = int(input("Number of sweets:  "))
if Number_of_sweets < 0:
    print("number of sweets cannot be negative")
elif Number_of_sweets < 1:
    print("Get some Sweets  first")
else:

    Number_of_students = int(input("Number of students:  "))
    Sweets_per_student = int(Number_of_sweets / Number_of_students)
    sweets_for_teachher = int(Number_of_sweets % Number_of_students)
    print("Each student will get {} sweets".format(Sweets_per_student))
    print("Teacher will get {} sweets".format(sweets_for_teachher))