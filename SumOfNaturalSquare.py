"""
Python Program to find sum of square of first N Natural Numbers.

Code:
"""

#Method-1
num = int(input("Enter A number :- "))
result = 0
for n in range(1, num+1):
    result = result + pow(n,2)
print("Square Of N Natural number = ", result)

#Method-2
num = int(input("Enter A number :- "))
result = 0
n=1
while(n<=num):
    result = result + pow(n,2)
    n = n+1
print("Square Of N Natural number = ", result)
