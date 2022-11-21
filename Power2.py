"""
Python Program to find Power of a number using while loop

Code:
"""

base = int(input("Enter base :- "))
exp = int(input("Enter exponent :- "))

result = 1
i=1
while(i<=exp):
    result = base * result
    i = i+1
print("Power = ", result)
