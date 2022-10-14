"""
Write a python program to check whether number is armstrong or not.

Code:
"""

num = int(input("Enter a number :- "))
temp = num
result = 0

lennum = len(str(num))

while(temp>0):
    lastdigit = temp % 10
    result = result + lastdigit ** lennum
    temp = temp // 10
if(result==num):
    print(num, " is Armstrong Number")
else:
    print(num, " is not Armstrong Number")
