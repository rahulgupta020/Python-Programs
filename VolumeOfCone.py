
"""
Python Program to find Volume of cone.

Code:
"""

import math
radius = int(input("Enter Radius :- "))
height = int(input("Enter height :- "))

result = math.pi * (radius*radius) * (height/3)
print("The Volume of cone = ",result)
