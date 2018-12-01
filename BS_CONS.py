#!/usr/bin/env python

# Consensus and Profile

# Problem
# A matrix is a rectangular table of values divided into rows and columns. An m×n matrix has m rows and n columns.
# Given a matrix A, we write Ai,j to indicate the value found at the intersection of row i and column j.
# Say that we have a collection of DNA strings, all having the same length n. Their profile matrix is a 
# 4×n matrix P in which P1,j represents the number of times that 'A' occurs in the jth position of one of 
# the strings, P2,j represents the number of times that C occurs in the jth position, and so on (see below).
#
#               A T C C A G C T
#               G G G C A A C T
#               A T G G A T C T
#  DNA Strings  A A G C A A C C
#               T T G G A A C T
#               A T G C C A T T
#               A T G G C A C T
#
#           A   5 1 0 0 5 5 0 0
#  Profile  C   0 0 1 4 2 0 6 1
#           G   1 1 6 3 0 1 0 0
#           T   1 5 0 0 0 1 1 6
#
# A consensus string c is a string of length n formed from our collection by taking the most common symbol 
# at each position; the jth symbol of c therefore corresponds to the symbol having the maximum value in the
# j-th column of the profile matrix. Of course, there may be more than one most common symbol, leading to
# multiple possible consensus strings.
# 
# Consensus	    A T G C A A C T
#
# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.
# Return: A consensus string and profile matrix for the collection. (If several possible consensus 
# strings exist, then you may return any one of them.)

# Sample Dataset
# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT
# Sample Output
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6
##########################
# Solution from Hazard
##########################
# Solution 1: use biopython's Bio.SeqIO module
# https://biopython.org/wiki/SeqIO
from Bio import SeqIO
import numpy as np
profile={}
for i in SeqIO.parse('rosalind_cons.txt', 'fasta'):
    dna=i.seq
    length=len(dna)
    if profile == {}:
        profile = dict(zip('ATGC', np.reshape([0] * (length* 4), [4,length]))) # init
    else:
        assert length == len(profile['A'])
    for j in range(length):
        #print(j)
        if dna[j] in profile:
            profile[dna[j]][j] += 1

consensus = ''.join([ list(profile.keys())[j] for j in np.argmax([i for i in profile.values()], axis= 0)])
print(consensus)
for k,v in profile.items():
    print(k, end=": ")
    print(' '.join([str(i) for i in v]))
    
# Solution 2: Advanced!
from Bio import SeqIO
matrix=zip(*[str(i.seq) for i in SeqIO.parse('rosalind_cons.txt', 'fasta')])
profile=map(lambda x: dict((i, x.count(i)) for i in 'ATGC'), matrix)
consensus=[max(i, key=i.get) for i in profile]
print(''.join(consensus))
#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 
