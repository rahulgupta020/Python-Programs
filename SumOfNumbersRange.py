"""
How do you find the sum of a given range of integers in python?

Code:
"""

startnum = int(input("Enter start number :- "))
endnum = int(input("Enter end number :- "))

result = 0
for num in range(startnum, endnum+1):
    result = result + num
print("Sum of numbers = ", result)
