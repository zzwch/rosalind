#!/usr/bin/env python

# Counting Point Mutations

# Problem
# Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), 
# is the number of corresponding symbols that differ in s and t. 
# Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
# Return: The Hamming distance dH(s,t).

# Sample Dataset
# GAGCCTACTAACGGGAT
# CATCGTAATGACGGCCT
# Sample Output
# 7

##########################
# Solution from Hazard
##########################
# Solution 1
def hamm(s, t):
    assert len(s)==len(t)
    d=0
    for i in range(0, len(s)):
        if s[i] != t[i]:
            d+=1
    return(d)

with open('rosalind_hamm.txt', 'r') as f:
    s=f.readline().strip()
    t=f.readline().strip()
    print(hamm(s,t))

# Solution 2

#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 
