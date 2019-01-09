#!/usr/bin/env python

# Finding a Shared Motif solved by 5878
# Problem
# A common substring of a collection of strings is a substring of every member of the collection.
# We say that a common substring is a longest common substring if there does not exist a longer 
# common substring. For example, "CG" is a common substring of "ACGTACGT" and "AACCGTATA", but 
# it is not as long as possible; in this case, "CGTA" is a longest common substring of "ACGTACGT" 
# and "AACCGTATA".
# Note that the longest common substring is not necessarily unique; for a simple example,
# "AA" and "CC" are both longest common substrings of "AACC" and "CCAA".

# Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
# Return: A longest common substring of the collection. (If multiple solutions exist, 
# you may return any single solution.)

# Sample Dataset
# >Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA
# Sample Output
# AC
##########################
# Solution from Hazard
##########################
# Solution 1
import numpy as np
import Bio.SeqIO

seqs = [str(seq.seq) for seq in Bio.SeqIO.parse('rosalind_lcsm.txt', 'fasta')]
# shortest
ref = seqs[np.argmin([len(i) for i in seqs])] 
# random
#ref = seqs[np.random.randint(0, len(seqs))]

def checkMotif(motif, seqs):
    for seq in seqs:
        if motif not in seq:
            return(False)
    return(True)

longest = ''
for start_ind in range(len(ref)):
    for end_ind in range(len(ref), start_ind, -1):
        motif = ref[start_ind:end_ind]
        if len(motif) <= len(longest):
            break
        if checkMotif(motif, seqs) and len(motif) > len(longest):
            longest = motif

print(longest)
#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 
