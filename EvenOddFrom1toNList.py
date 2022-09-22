"""
Python program to print even and odd numbers from 1 to n using list.

Code:
"""

num = int(input("Enter N value :- "))

evenList=[]
oddList=[]
for n in range(1, num+1):
    if(n%2==0):
        evenList.append(n)
    elif(n%2!=0):
        oddList.append(n)
print("Even = ", evenList)
print("Odd = ", oddList)
