"""
Python – Largest of Three Numbers

Code:
"""

num1 = int(input("Enter num1 :- "))
num2 = int(input("Enter num2 :- "))
num3 = int(input("Enter num3 :- "))

if(num1>=num2) and (num1>=num3):
    print(num1, "is Greater")
elif(num2>=num1) and (num2>=num3):
    print(num2, "is Greater")
else:
    print(num3, "is Greater")
