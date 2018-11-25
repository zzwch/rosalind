#!/usr/bin/env python

# Strings and Lists

# Problem
# Given: A string s of length at most 200 letters and four integers a, b, c and d.
# Return: The slice of this string from indices a through b and c through d (with space in between), inclusively. In other words, we should include elements s[b] and s[d] in our slice.

# Sample Dataset
# HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain.
# 22 27 97 102
# Sample Output
# Humpty Dumpty

a=22 
b=27 
c=97 
d=102 
text='HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain'
print(text[a:b+1], text[c:d+1]) # use `print text[a:b+1], text[c:d+1]` in python2

'''
>>> a=22 
>>> b=27 
>>> c=97 
>>> d=102 
>>> text='HumptyDumptysatonawallHumptyDumptyhadagreatfallAlltheKingshorsesandalltheKingsmenCouldntputHumptyDumptyinhisplaceagain'
>>> print(text[a:b], text[c:d])
Humpt Dumpt
>>> print(text[a:b+1], text[c:d+1])
Humpty Dumpty
'''
