#!/bin/python
"""
Project Euler Problem 40

Alistair Ferguson - 10.12.2014

Champernowne's constant
"""

def euler40():
    """ Project Euler problem 40 main."""
    # Generate Champs number up to 1m places in the fraction
    champ = '0.1'
    num = 1
    while len(champ) < (10**6 + 2):
        num += 1
        champ = "%s%s" % (champ, num)

    # Calculate expression
    multiplication = 1
    lst = []
    for x in [1,10,100,1000,10**4,10**5,10**6]:
        # +1 to skip 0.
        multiplication *= int(champ[x+1])
        lst.append(int(champ[x+1]))

    print "solution: %s" % multiplication

if __name__ == "__main__":
    euler40()
