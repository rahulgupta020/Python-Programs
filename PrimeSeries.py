"""
Print prime numbers within an interval.

Code:
"""

startnum = int(input("Enter start number :- "))
endnum = int(input("Enter end number :- "))

for num in range(startnum, endnum+1):
    for n in range(2, num):
        if(num%n)==0:
            break
    else:
        print(num, end=" ")
print()
