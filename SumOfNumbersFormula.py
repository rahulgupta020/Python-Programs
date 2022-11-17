"""
How do you find the sum of a given range of integers using formula in python?

Code:
"""

num1 = int(input("Enter Start Number :- "))
num2 = int(input("Enter End Number :- "))

result = int((num2*(num2+1)/2) - (num1*(num1+1)/2) + num1)
print("Sum of num1 to num2 :- ", result)
