"""
 Improved version of  Displaying the result of a Student
 Displaying Highest, Lowest and Average marks scored

"""

report_card = []

students_name = input("enter students name: ").capitalize()
number_of_subjects = int(input("Enter number of subjects:  "))

counter = 1
while counter != number_of_subjects + 1:
    marks = int(input("Enter marks of Subject " + str(counter) + ": " ))
    report_card.append(marks)
    counter = counter + 1

Highest_mark = max(report_card)
lowest_mark = min(report_card)
average_mark = (sum(report_card)/number_of_subjects)
print("HELLO! {} , here is your exam result".format(students_name))
print("The highest marks you have scored are {} , Well done! ".format(Highest_mark))
print("The Lowest marks you have scored are {} , Better luck next time! ".format(lowest_mark))
print("Your average marks are {} ".format(average_mark))