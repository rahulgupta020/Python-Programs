"""
Python program to count number of vowels in string.

Code:
"""

#Method-1
string = input("Enter a string :- ")

countVowels = 0
for ch in string:
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U'):
        countVowels = countVowels+1
print("Total Vowels Count are = ", countVowels)


#Method-2
string = input("Enter a string :- ")

countVowels = 0
for ch in string:
    if ch in "aeiouAEIOU":
        countVowels = countVowels+1
print("Total Vowels Count are = ", countVowels)
