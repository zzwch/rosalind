#!/usr/bin/env python

# Complementing a Strand of DNA

# Problem
# In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.
# The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s, 
# then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

# Given: A DNA string s of length at most 1000 bp.
# Return: The reverse complement sc of s.
# Sample Dataset
# AAAACCCGGT
# Sample Output
# ACCGGGTTTT

##########################
# Solution from Hazard
##########################
# Solution 1
s='AAAACCCGGT'
d={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
for i in reversed(s): 
    print(d[i], end='')

print('\n')

# Solution 2
s='AAAACCCGGT'
d={'A':'T', 'T':'A', 'G':'C', 'C':'G'}
sc=[]
for i in reversed(s): 
    sc.append(d[i])

print(''.join(sc))

# Solution 3
with open('rosalind_revc.txt', 'r') as f:
    s=f.readline().strip()
    print(s.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()[::-1]) # Option 1
    # print(s.translate(str.maketrans('ATGC','TACG'))[::-1]) # Option 2

#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 
