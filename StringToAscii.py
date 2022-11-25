"""
Python Program to convert string to ascii

Code:
"""

str = input("Enter a string :- ")

for ch in str:
    result = ord(ch)
    print(result, end=" ")
