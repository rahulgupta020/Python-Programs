"""
Python program to convert decimal to binary

Code:
"""

dec = int(input("Enter Decimal Number :- "))
result = bin(dec).replace("0b", "")
print("Binary Number = ", result)
