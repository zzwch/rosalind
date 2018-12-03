#!/usr/bin/env python

# Mortal Fibonacci Rabbits
# Problem
# Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”,
# which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits 
# reaches maturity in one month and produces a single pair of offspring (one male, one female) 
# each subsequent month.

# Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution 
# in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction
# of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice 
# before dying).

# Given: Positive integers n≤100 and m≤20.
# Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

# Sample Dataset
# 6 3
# Sample Output
# 4
##########################
# Solution from Hazard
##########################
# Solution 1
def fib(n, m, M):
    assert M >= 3
    if m == 1:
        if n == 1:
            return(1)
        elif n == 2:
            return(0)
        elif n >= 3:
            fn1 = 0
            for i in range(2,M+1):
                fn1 += fib(n-1, i, M)
            return(fn1)
    if n < m :
        return(0)
    else:
        return(fib(n-1, m-1, M))

def FIB(N, M):
    fn = 0
    for i in range(1,M+1):
        fn += fib(N, i, M)
    return(fn)
    
#########################################################
# you may add your solutions below
# Don't hesitate to send pull request for your new solution 
