#!/usr/bin/env python

# Intro to Python dictionary
# Problem
# Given: A string s of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces. 
# Words are case-sensitive, and the lines in the output can be in any order.
#
# Sample Dataset
# We tried list and we tried dicts also we tried Zen
# Sample Output
# and 1
# We 1
# tried 3
# dicts 1
# list 1
# we 2
# also 1
# Zen 1

# Solution 1
s='We tried list and we tried dicts also we tried Zen'
d={}
for i in s.split(' '):
  if i in d: # 'dict' object has no attribute 'has_key' in python3
    d[i] += 1
  else:
    d[i] = 1

for k, v in d.items():
  print(k, v)
  
'''
>>> s='We tried list and we tried dicts also we tried Zen'
>>> d={}
>>> for i in s.split(' '):
...   if i in d: # 'dict' object has no attribute 'has_key' in python3
...     d[i] += 1
...   else:
...     d[i] = 1
... 
>>> for k, v in d.items():
...   print(k, v)
... 
We 1
tried 3
list 1
and 1
we 2
dicts 1
also 1
Zen 1
'''

# Solution 2
# On the Shoulders of Giants you can also try the following
# https://docs.python.org/2/library/collections.html
from collections import Counter 
s='We tried list and we tried dicts also we tried Zen'
for k,v in Counter(s.split(' ')).items():
  print(k, v)

'''
>>> from collections import Counter 
>>> s='We tried list and we tried dicts also we tried Zen'
>>> for k,v in Counter(s.split(' ')).items():
...   print(k, v)
... 
We 1
tried 3
list 1
and 1
we 2
dicts 1
also 1
Zen 1
'''



## solutions from hejian @20181127
>>> text = 'We tried list and we tried dicts also we tried Zen'
>>> word = text.split(" ")
>>> set = set(word)
>>> word1 = list(set)
>>> dir = {}
>>> for x in range(len(word1)):
...     dir[word1[x]] = 0
...     for y in range(len(word)):
...             if word1[x] == word[y]:
...                     dir[word1[x]] += 1
...
>>> print(dir)
>>> for i, j in dir.items():
...     print(i, j)
...


