#!/usr/bin/python
'''
Project Euler
Problem 29 
'''
lst = []

for a in range(2, 101):
    for b in range(2, 101):
        lst.append(a**b)

print len(set(lst))
