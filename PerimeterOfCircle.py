"""
Python program to find the perimeter of a circle

Code:
"""

#Method-1
r = float(input("Enter A redius :- "))

perimeter = 2 * 3.14 * r
print("Perimeter of circle = ",perimeter)



#Method-2
import math
r = float(input("Enter A redius :- "))

perimeter = 2 * math.pi * r
print("Perimeter of circle = ",perimeter)
