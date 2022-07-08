"""
Python program to find algebric formula i.e (a+b)3 = a3 + b3 + 3a2b + 3ab2

Code:
"""

a = int(input("Enter A Value :- "))
b = int(input("Enter B Value :- "))

result1 = (a**3) + (b**3) + ((3*a*b)*(a+b))
print("The Result = ", result1)
