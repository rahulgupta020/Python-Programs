"""
Program to create grade calculator in Python

Code:
"""

hindi = float(input("Enter Hindi Marks :- "))
english = float(input("Enter english Marks :- "))
math = float(input("Enter math Marks :- "))
it = float(input("Enter it Marks :- "))

total = hindi+english+math+it
per = (total/400)*100
print("Total Marks = ", total)
print("Percentage = ", per)
