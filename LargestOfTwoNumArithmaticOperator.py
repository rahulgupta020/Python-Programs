"""
Largest of two number using arithmatic operator in python

Code:
""" 

num1 = int(input("Enter num1 :- "))
num2 = int(input("Enter num2 :- "))

if(num1-num2>0):
    print(num1, " is Greater")
elif(num2-num1>0):
    print(num2, " is Greater")
else:
    print("Both numbers are equal")
