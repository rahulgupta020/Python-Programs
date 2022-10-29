"""
Python: Calculate sum of square of digits of a number.

Code:
"""

#Method-1
num = int(input("Enter a number :- "))
result = 0

while(num>0):
    lastdigit = num % 10
    result = result + lastdigit*lastdigit
    num = num // 10
print("Sum of Square Of Digits are = ", result)


#Method-2
num = int(input("Enter a number :- "))
result = 0

for i in range(0, len(str(num))):
    lastdigit = num % 10
    result = result + lastdigit*lastdigit
    num = num // 10
print("Sum of Square Of Digits are = ", result)
