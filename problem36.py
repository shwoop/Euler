#!/bin/python
"""
Project Euler Problem 36

A. Ferguson - 10-12-2014

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in
base 10 and base 2.  (Please note that the palindromic number, in either base,
may not include leading zeros.)
"""

def reverse_number(num):
    """ Reverse number. """
    return str(num)[::-1]


def problem_36():
    """ Project Euler Problem 36 main. """
    running_total = 0
    for num in range(1,1000000):
        if str(num) == reverse_number(num) and \
                bin(num)[2:] == reverse_number(bin(num)[2:]):
            print "num %s bin %s" % (num, bin(num)[2:])
            running_total = running_total + num
    print "solution: %s" % running_total

if __name__ == "__main__":
    problem_36()
