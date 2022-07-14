"""
Python Program to Calculate Simple Interest.

Code:
"""

P = float(input("Enter Principal Value :- "))
R = float(input("Enter Rate of Interest :- "))
T = float(input("Enter Time Period :- "))

simple_interest = (P*R*T)/100
print("Simple Interest = ", simple_interest)
print("Total amount paid after 1 year = ", simple_interest+P)
