#!/usr/bin/env python

# Calculating Expected Offspring
#
# Problem
#
# For a random variable X taking integer values between 1 and n, the expected value of X is 
# E(X)=∑nk=1k×Pr(X=k). The expected value offers us a way of taking the long-term average of 
# a random variable over a large number of trials.
#
# As a motivating example, let X be the number on a six-sided die. Over a large number of rolls, 
# we should expect to obtain an average of 3.5 on the die (even though it's not possible to roll 
# a 3.5). The formula for expected value confirms that E(X)=∑6k=1k×Pr(X=k)=3.5.
#
# More generally, a random variable for which every one of a number of equally spaced outcomes 
# has the same probability is called a uniform random variable (in the die example, this "equal spacing" 
# is equal to 1). We can generalize our die example to find that if X is a uniform random variable with 
# minimum possible value a and maximum possible value b, then E(X)=a+b2. You may also wish to verify that
# for the dice example, if Y is the random variable associated with the outcome of a second die roll, then E(X+Y)=7.

# Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the 
# number of couples in a population possessing each genotype pairing for a given factor. In order, 
# the six given integers represent the number of couples having the following genotypes:
# 1. AA-AA
# 2. AA-Aa
# 3. AA-aa
# 4. Aa-Aa
# 5. Aa-aa
# 6. aa-aa
# Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
# under the assumption that every couple has exactly two offspring.

# Sample Dataset
# 1 0 0 1 0 1
# Sample Output
# 3.5
##########################
# Solution from Hazard
##########################
# Solution 1
with open('rosalind_iev.txt') as f:
    couple = [int(i) for i in f.readline().strip().split()]
    probs = [1, 1, 1, 3/4, 1/2, 0]
    print(sum(2*[couple[i]*probs[i] for i in range(len(probs))]))
    
# Solution 2: same as Solution 1, except using numpy
import numpy as np
offspring = 2
with open('rosalind_fibd.txt') as f:
    couple = np.array([int(i) for i in f.readline().strip().split()])
    probs = np.array([1, 1, 1, 3/4, 1/2, 0])
    print(offspring*np.dot(couple, probs))
#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 
