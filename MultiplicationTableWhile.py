"""
Multiplication Table using while loop in python.

Code:
"""

num = int(input("Enter a number :- "))

count = 1
while(count<=10):
	print(num ,"*", count ,"=", count*num)
	count = count + 1
