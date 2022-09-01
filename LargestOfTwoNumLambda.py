"""
Python Program To Find The Largest Among Two Number Using Lambda Functon.

Code:
"""

num1 = int(input("Enter num1 :- "))
num2 = int(input("Enter num2 :- "))

result = lambda num1,num2 : num1 if(num1>=num2) else num2
print(result(num1, num2), " is Greater")
