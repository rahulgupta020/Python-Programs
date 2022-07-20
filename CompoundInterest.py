"""
Python program to find compound interest

Code:
"""

P = float(input("Enter Principal :- "))
R = float(input("Enter Rate of Interest :- "))
T = float(input("Enter Time Period :- "))

amount = P*(pow((1+R/100),T))
ci = amount-P
print("Compound Interest = ", ci)
print("Total amount you have to paid = ", amount)
