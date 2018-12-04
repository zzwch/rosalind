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
...         if word1[x] == word[y]:
...             dir[word1[x]] += 1
...
>>> print(dir)
>>> for i, j in dir.items():
...     print(i, j)
...


## results from hehan @20181204
>>> c = 'When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be'
>>> c = c.split()
>>> d = {}
>>> for word in c:
...     if word in d:
...         d[word] += 1
...     else:
...         d[word] = 1
...
>>> print(d)
>>> for key, value in d.items():
...     print(key,value)
...

