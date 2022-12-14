"""
Python program for sum of cube of first N natural numbers

Code:
"""

#Method-1
num = int(input("Enter a number :- "))
result = 0
for n in range(1, num+1):
    result = result + pow(n,3)
print("Cube of natural number = ", result)

#Method-2
num = int(input("Enter a number :- "))
result = 0
n=1
while(n<=num):
    result = result + pow(n,3)
    n=n+1
print("Cube of natural number = ", result)
