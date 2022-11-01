"""
Python Program to check character is a vowel or consonant

Code:
"""

ch = input("Enter a Character :- ")

if(len(ch)==1 and ch.isalpha()):
    if(ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U"):
        print(ch, " is Vowel")
    else:
        print(ch, " is Not Vowel")
else:
    print("Invalid!!! Please Enter a Character")
