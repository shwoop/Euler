#!/usr/bin/python
'''
Project Euler
Problem 24
'''

from itertools import permutations

x = permutations('0123456789')
x = [i for i in x]
#print x[1000000]
print x[999999]
