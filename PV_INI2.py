#!/usr/bin/env python

# Variables and Some Arithmetic

# You can now use all common arithmetic operations involving numbers:
# Addition: 2 + 3 == 5
# Subtraction: 5 - 2 == 3
# Multiplication: 3 * 4 == 12
# Division: 15 / 3 == 5
# Division remainder: 18 % 5 == 3
# Exponentiation: 2 ** 3 == 8
# It is important to note that if you try to divide two integers, Python always rounds down the result (so 18/5 == 3).

# Problem
# Given: Two positive integers a and b, each less than 1000.
# Return: The integer corresponding to the square of the hypotenuse of the right triangle whose legs have lengths a and b.

# Sample Dataset
# 3 5
# Sample Output
# 34

a=3
b=5
c=a**2+b**2
print(c)

'''
>>> a=3
>>> b=5
>>> c=a**2 + b**2
>>> print(c)
34
'''
