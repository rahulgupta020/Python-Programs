"""
Python program to convert decimal to binary

Code:
"""

num = int(input("Enter Decimal = "))

result=""
while(num>0):
    result = result + str(num&1)
    num = num >> 1
result = result[::-1]
print("Binary Number = ", result)
