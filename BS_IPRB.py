#!/usr/bin/env python

# Mendel's First Law

# Problem
# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
# k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual 
# possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

# Sample Dataset
# 2 2 2
# Sample Output
# 0.78333

##########################
# Solution from Hazard
##########################
# Solution 1: straight forward computaion 
# scipy.special has large amount of useful math functions including all from numpy 
import scipy.special as sps
def prob(k:int, m:int, n:int):
    return(1 - (sps.comb(n, 2) + 0.25* sps.comb(m, 2) +0.5*m*n)/sps.comb(k+m+n, 2)) 

print(prob(2,2,2))

#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 
