"""
Python program to find algebric formula i.e (a+b+c)2 = a2+b2+c2+2ab+2bc+2ca

Code:
"""

a = int(input("Enter A Value :- "))
b = int(input("Enter B Value :- "))
c = int(input("Enter c Value :- "))

result1 = (a*a) + (b*b) + (c*c) + (2*a*b) + (2*b*c) + (2*c*a)
print("The Result = ",result1)
