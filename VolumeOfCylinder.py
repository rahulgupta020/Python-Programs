"""
Python Program to find Volume of a Cylinder.

Code:
"""

import math
radius = int(input("Enter Radius :- "))
height = int(input("Enter height :- "))

result = math.pi * radius*radius *height
print("Volume of Cylinder = ", result)
