"""
Python program to convert binary to decimal

Code:
"""

bin_num = list(input("Enter Binary Number :- "))

result = 0
for i in range(len(bin_num)):
    last_digit = bin_num.pop()
    result = result + int(last_digit) * pow(2, i)
print("Binary Number = ", result)
