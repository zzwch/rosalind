#!/usr/bin/env python

# Translating RNA into Protein
# Problem
# The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English alphabet 
# (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from these 20 symbols. 
# Henceforth, the term genetic string will incorporate protein strings along with DNA strings and RNA strings.

# The RNA codon table dictates the details regarding the encoding of specific codons into the amino acid alphabet.
# Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).
# Return: The protein string encoded by s.

# Sample Dataset
# AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
# Sample Output
# MAMAPRTEINSTRING

##########################
# Solution from Hazard
##########################
# Solution 1
codon_table='''
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G
'''.replace('\n', ' ').split(' ')
codon_table=[i for i in codon_table if i != '']

codon_dict={}
codon_dict=dict(zip(codon_table[::2], codon_table[1::2]))

with open('rosalind_prot.txt', 'r') as f:
    rna=f.readline().strip()
    for i in range(0, len(rna), 3):
        aa=codon_dict[rna[i:i+3]]
        if aa == "Stop":
            break
        else:
            print(aa,end="")

#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 
