"""
Write a program to reverse digits of a number

Code:
"""

num = int(input("Enter a number :- "))

revnum = 0
while(num>0):
    lastdigit = num % 10
    revnum = (revnum*10)+lastdigit
    num = num // 10
print("Reversed Number = ", revnum)
