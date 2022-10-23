"""
Python: Calculate sum of digits of a number.

Code:
"""

num = int(input("Enter a number :- "))
result = 0

while(num>0):
    lastdigit = num % 10
    result = result + lastdigit
    num = num // 10
print("The Sum of digits are = ", result)
