"""
Python program to print even or odd numbers from 1 to n.

Code:
"""

num = int(input("Enter N Value :- "))

print("Even Numbers are = ")
for n in range(1, num+1):
    if(n%2==0):
        print(n)

print("\nOdd Numbers are = ")
for n in range(1, num+1):
    if(n%2!=0):
        print(n)
