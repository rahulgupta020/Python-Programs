"""
Python program to convert binary to decimal

Code:
"""

bin_num = int(input("Enter Binary :- "))

result = 0
i=0
while(bin_num>0):
    last_digit = bin_num%10
    result = result + last_digit*pow(2,i)
    bin_num = bin_num//10
    i = i+1
print("Decimal Number = ", result)
