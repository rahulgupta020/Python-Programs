"""
Python Program to Multiplication Table in Given Range.

Code:
"""

startnum = int(input("Enter a start number :- "))
endnum = int(input("Enter a end number :- "))

for num in range(startnum, endnum+1):
    for counter in range(1, 10+1):
        print(num ,"*", counter ,"=", counter*num)
    print()

