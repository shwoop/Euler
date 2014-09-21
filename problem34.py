#!/usr/bin/python
'''
Project Euler
Problem 34
'''

from math import factorial


# memoize factorial function for 0-9
fact = [factorial(x) for x in range(0,10)]


def num_equals_fact_of_digits(num):
    '''
    Test if given number equals the sum of the factorials of the digits of the
    number.
    eg.
        145 = 1! + 4! + 5!
            = 1 + 24 + 120
            = 145
    '''
    running_total = 0

    for digit in str(num):
        running_total = running_total + fact[int(digit)]
        #print 'num: %d, digit: %s, total: %d' % (num, digit, running_total)

        # break once we go over the given number
        if running_total > num:
            return False

    if running_total == num:
        return True

    return False


if __name__ == "__main__":
    running_total = 0
    # process for 1'000'000 as sum probably gets too big with so many digits
    for x in range(3, 1000000):
        if num_equals_fact_of_digits(x):
            running_total = running_total + x

    print running_total
