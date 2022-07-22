"""
Python Program to find lcm of two number

Code:
"""
num1 = int(input("Enter num1 :- "))
num2 = int(input("Enter num2 :- "))

if(num1>num2):
    maxnum = num1
else:
    maxnum = num2
temp = maxnum
# maxnum = max(num1,num2)

count = 0
while(True):
    if(maxnum%num1==0 and maxnum%num2==0):
        break
    maxnum = maxnum+temp
    count = count+1
print("LCM is = ", maxnum)
print("Total loop = ", count)

print("\nMethod -2\n")



num1 = int(input("Enter num1 :- "))
num2 = int(input("Enter num2 :- "))

if(num1>num2):
    maxnum = num1
else:
    maxnum = num2

# maxnum = max(num1,num2)

count = 0
while(True):
    if(maxnum%num1==0 and maxnum%num2==0):
        break
    maxnum = maxnum+1
    count = count+1
print("LCM is = ", maxnum)
print("Total loop = ", count)
