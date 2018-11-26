#!/usr/bin/env python

# Reading and Writing
# To access a file, you must first open it. To do so, you can use the open() function, 
# which takes two parameters: the name of the target file and the mode. Three modes are available:
# r - read mode (the file is opened for reading)
# w - write mode (the file is opened for writing, and if a file having the same name exists, it will be erased)
# a - append mode (the file is opened for appending, which means that data is only to be added to the existing data in the file)
# f = open('input.txt', 'r')
# f.read(n) returns n bytes 
# f.readline() takes a single line
# f.readlines() returns a list containing every line 
# .strip() method
# .split() method
# f.write('string you want to write into file')
# don't forget that you must close it using the command f.close().

# Problem
# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.
#
# Sample Dataset
# Bravely bold Sir Robin rode forth from Camelot
# Yes, brave Sir Robin turned about
# He was not afraid to die, O brave Sir Robin
# And gallantly he chickened out
# He was not at all afraid to be killed in nasty ways
# Bravely talking to his feet
# Brave, brave, brave, brave Sir Robin
# He beat a very brave retreat
#
# Sample Output
# Yes, brave Sir Robin turned about
# And gallantly he chickened out
# Bravely talking to his feet
# He beat a very brave retreat

with open('output.txt', 'w') as fo:
  with open('input.txt', 'r') as fi:
    while fi.readline():
      fo.write(fi.readline())

'''
>>> with open('output.txt', 'w') as fo:
...   with open('input.txt', 'r') as fi:
...     while fi.readline():
...       fo.write(fi.readline())
... 
34
31
28
29
# see output.txt 
'''

## results from hejian @20181127
>>> file = open('./Rosalind/rosalind_ini5.txt')
>>> lines = file.readlines()
>>> i = 0
>>> for line in lines:
...     i += 1
...     if i % 2 == 0:
...             print(line)
...

