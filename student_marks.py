"""
 Displaying the result of a Student
 Displaying Highest, Lowest and Average marks scored

"""


students_name = input("enter students name: ").capitalize()
First_mark = int(input("Enter marks scored: "))
second_mark = int(input("Enter marks scored: "))
third_mark = int(input("Enter marks scored: "))
Fourth_mark = int(input("Enter marks scored: "))

marks = [First_mark,second_mark,third_mark,Fourth_mark]
Highest_mark = max(marks)
lowest_mark = min(marks)
average_mark = (sum(marks)/4)
print("HELLO! {} , here is your exam result".format(students_name))
print("The highest marks you have scored are {} , Well done! ".format(Highest_mark))
print("The Lowest marks you have scored are {} , Better luck next time! ".format(lowest_mark))
print("Your average marks are {} ".format(average_mark))
