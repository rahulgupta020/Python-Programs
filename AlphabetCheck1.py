"""
Python program to check character is alphabet or not using ASCII Values

Code:
"""

ch = input("Enter a Character :- ")

if(ord(ch)>=65 and ord(ch)<=90) or (ord(ch)>=97 and ord(ch)<=122):
    print(ch, " is Alphabet")
else:
    print(ch, " is not Alphabet")
