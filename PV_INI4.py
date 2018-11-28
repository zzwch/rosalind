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

## results from hejian @20181127
>>> sum = 0
>>> for i in range(101, 200, 2):
...     sum += i
...
>>> print(sum)
7500


>>> sum = 0
>>> for i in range(4211, 8876, 2):
...     sum += i
...
>>> print(sum)
15264819


