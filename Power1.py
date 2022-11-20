"""
Python Program to find Power of a number

Code:
"""

base = int(input("Enter base :- "))
exp = int(input("Enter Exponent :- "))

result = 1
for i in range(1, exp+1):
    result = base * result
print("Power = ", result)
