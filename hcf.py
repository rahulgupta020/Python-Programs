"""
Python Program to find hcf of two number

Code:
"""
num1 = int(input("Enter num1 :- "))
num2 = int(input("Enter num2 :- "))

if(num1<num2):
    smallnum = num1
else:
    smallnum = num2
#smallnum = min(num1, num2)
print(smallnum)

for i in range(1, smallnum+1):
    if(num1%i==0 and num2%i==0):
        hcf = i

print("The HCF = ", hcf)
