"""
Python Math: Add, subtract, multiply and divide two fractions using Fraction Module in Python

Code:
"""

import fractions

A = int(input())
B = int(input())
C = int(input())
D = int(input())

f1 = fractions.Fraction(A, B)
f2 = fractions.Fraction(C, D)

print("Addition Fraction = ", f1+f2)
print("Subtraction Fraction = ", f1-f2)
print("Multiplication Fraction = ", f1*f2)
print("Division Fraction = ", f1/f2)
