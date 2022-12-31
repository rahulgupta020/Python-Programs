"""
Python Program to find Perfect Number or Not

Code:
"""

num = int(input("Enter a number :- "))

result = 0
for i in range(1, num):
    if(num%i==0):
        result = result + i
if(result==num):
    print(num, "is Perfect Number")
else:
    print(num, "is not Perfect Number")
