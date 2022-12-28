"""
Python Program to Check Leap Year using Calendar Module.

Code:
"""

import calendar

year = int(input("Enter a year :- "))
result = calendar.isleap(year)
if(result):
    print(year, "is Leap Year")
else:
    print(year, "is not Leap Year")
