"""
  Diving the total number of Sweets among total number of students
  The remaining sweets are given to the teacher

"""


Number_of_sweets = 32
Number_of_students = 15
Sweets_per_student = int(Number_of_sweets/Number_of_students)
Sweets_teacher = int(Number_of_sweets % Number_of_students)

print("Each student will get {} sweets".format(Sweets_per_student))
print("And the teacher will get {} sweets".format(Sweets_teacher))