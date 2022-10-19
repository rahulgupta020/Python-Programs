"""
How to Check a Number is Palindrome in Python?

Code:
"""

num = int(input("Enter a number :- "))
temp = num
rev = 0

while(num>0):
    lastdigit = num % 10
    rev = rev*10 + lastdigit
    num = num // 10
if(rev==temp):
    print(temp, " is Palindrome Number")
else:
    print(temp, "is not Palindrome Number")
