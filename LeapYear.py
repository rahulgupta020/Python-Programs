"""
Python Program to check year is leap year or not.

Code:
"""

year = int(input("Enter Year :- "))

if(year%400==0) or (year%4==0 and year%100!=0):
    print(year, "is Leap Year")
else:
    print(year, "is not Leap Year")
