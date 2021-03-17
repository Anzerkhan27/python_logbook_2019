"""

Calculating the number of Computer labs for total number of students(Improved Version)

"""


from math import ceil
try:
    number_of_students = int(input("Enter number of students: \n "))
    while number_of_students < 1:
        print("there need to be some students in the first place ")
        number_of_students = int(input("Enter number of students: \n "))

    number_of_pc_each_lab = int(input("Enter number of pc's in each lab: \n "))
    while number_of_pc_each_lab < 1:
        print(" there need to be some desktops in a lab ")
    number_of_labs = ceil(number_of_students / number_of_pc_each_lab)
    if number_of_labs > 1:
        print("you will need {} labs for all the students".format(number_of_labs))
    else:
        print("you will need 1 lab for all the students")
except: print("enter an integer")

