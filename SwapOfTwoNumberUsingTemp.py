"""
Write a python program to swap of two number using third variable or temp variable.

Code:
"""

num1 = int(input("Enter num1 :- "))
num2 = int(input("Enter num2 :- "))

temp = num1
num1 = num2
num2 = temp

print("\nAfter Swapping\n")
print("Num1 = ", num1)
print("Num2 = ", num2)
