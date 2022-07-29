"""
Write a python program to swap of two number without using third variable or temp variable.

Code:
"""

num1 = int(input("Enter num1 :- "))
num2 = int(input("Enter num2 :- "))

num1 = num1+num2
num2 = num1-num2
num1 = num1-num2

print("\nAfter Swapping\n")
print("Num1 = ", num1)
print("Num2 = ", num2)
