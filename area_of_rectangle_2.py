"""
   Modified Version of Calculating Area of a Rectangle
   User cannot enter negative Length and breadth

"""



length_one = int(input("ENTER FIRST LENGTH IN CM: "))
while length_one < 1:
    print("Enter a postive non zero integer ")
    length_one = int(input("ENTER FIRST LENGTH IN CM: "))

length_two = int(input("ENTER SECOND LENGTH IN CM: "))
while length_two < 1:
    print("Enter a postive non zero integer ")
    length_two = int(input("ENTER SECOND LENGTH IN CM: "))
area = (length_one * length_two)

print("The Area of the given rectangle is {} cm^2 ".format(area))
