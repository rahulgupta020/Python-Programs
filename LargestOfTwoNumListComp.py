"""
Python Program To Find The Largest Among Two Number Using list comprehension.

Code:
"""

num1 = int(input("Enter num1 :- "))
num2 = int(input("Enter num2 :- "))

result = [ num1 if(num1>=num2) else num2 ]
print(result, " is Greater")
