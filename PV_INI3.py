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

##results from hejian @20181126
>>> a="lm19qicswxRq03jTf1dRJsNfZmgObzk1XRUdKOVMdxMTpb9EPLOXbNJCbvvsfPelecanusQhqJ2NWw1z0ZCdH9Sj3KFhNu45kDNdlHg7altaicao8NTJaGpf4i5qfrNpthlRkeuDNO1vo053wsz7YkUcBOqov3yx3mOhm55e."
>>> print(a[61:70],a[104:111])
Pelecanus altaica
...


## results from hehan @20181204
'''
>>> a = 'kRRhPUvZx8vITX9FoJWYOXuRLNhVxjLU8tGonocephalus2Uw67gDlpQyIiTKUu675RMKPKV6rPTKezTN7HcTGJ11K8G0FuHJYZaHyPAEvJebQ7U4fT5yZQEwF0N46NYMJvuio3Y00YcpulcherTKf6uCgKz6JNN'
>>> print(a[34:46],a[140:147])
Gonocephalus pulcher
'''
