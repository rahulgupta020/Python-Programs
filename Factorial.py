"""
Write a python program to find Factorial of a number.

Code:
"""

n = int(input("Enter a number :- "))

fact = 1
for i in range(n):
    fact = fact * n
    n = n - 1
print("Factorial of a given number = ", fact)
