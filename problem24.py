#!/usr/bin/python
'''
Project Euler
Problem 24
'''

from itertools import permutations

perms = permutations('0123456789')
perms = list(perms)

# print 'solution: %s' % perms[999999]
print 'solution: %s' % ''.join(perms[999999])
