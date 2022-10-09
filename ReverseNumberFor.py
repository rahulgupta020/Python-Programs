"""
Write a program to reverse digits of a number using For Loop

Code:
"""

num = int(input("Enter a number :- "))

revnum = 0
for i in range(0, len(str(num))):
    lastdigit = num % 10
    revnum = (revnum*10)+lastdigit
    num = num // 10
print("Reversed Number = ", revnum)
