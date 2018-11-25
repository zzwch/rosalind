#!/usr/bin/env python

# Conditions and Loops

# Problem
# Given: Two positive integers a and b (a<b<10000).
# Return: The sum of all odd integers from a through b, inclusively.

# Sample Dataset
# 100 200
# Sample Output
# 7500

a=100
b=200
s=0
for i in range(a, b+1):
  if i%2 == 1:
    s += i

print(s)

'''
>>> a=100
>>> b=200
>>> s=0
>>> for i in range(a, b+1):
...   if i%2 == 1:
...     s += i
... 
>>> print(s)
7500
>>> 
'''
