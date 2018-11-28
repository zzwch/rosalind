#!/usr/bin/env python

# Transcribing DNA into RNA

# Problem
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.
# Given a DNA string t corresponding to a coding strand, its transcribed RNA string u is 
# formed by replacing all occurrences of 'T' in t with 'U' in u.

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t.
# Sample Dataset
# GATGGAACTTGACTACGTAAATT
# Sample Output
# GAUGGAACUUGACUACGUAAAUU

#############################
# Solution from Hazard
#############################
# Solution 1
t='GATGGAACTTGACTACGTAAATT'
print(t.replace('T','U'))

# Solution 2
t='GATGGAACTTGACTACGTAAATT'
tt=''
for i in t:
  if i == 'T':
    tt += 'U'
  else:
    tt += i

print(tt)

#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 
