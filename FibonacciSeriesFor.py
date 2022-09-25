"""
Python Program to Print the Fibonacci sequence

Code:
"""

n = int(input("Enter a number :- "))

n1 = 0
n2 = 1

print("Fibonacci Series are = ",n1, n2, end=" ")
for i in range(3, n+1):
    n3 = n1+n2
    n1=n2
    n2=n3
    print(n3, end=" ")
print()
