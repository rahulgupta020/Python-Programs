"""
Sum of First N Natural Numbers in Python

Code:
"""

num = int(input("Enter N Value :- "))

sum = 0
while(num>0):
    sum = sum + num
    num = num - 1
print("Sum of n natural number = ",sum)
