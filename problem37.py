#!/usr/bin/python
'''
Project Euler
Problem 37
'''


from util import PrimeSieve


__directions = ['LEFT','RIGHT']


def permutations_removing_end_digit(direction, num):
    ''' Generate list of numbers from seeding num where digits are
        trimmed from the desired end. '''
    assert direction in __directions, 'Invalid direction.  Use CAPS.'

    permutations = [num]
    str_num = str(num)
    for i in range(1,len(str_num)):
        if direction is 'LEFT':
            permutations.append(str_num[i:])
        else:
            permutations.append(str_num[:i])

    return permutations


def is_two_way_truncatable_prime(sieve, num):
    ''' Given a number.  Test all trimmed permutations for primality. '''
    permutations = permutations_removing_end_digit('LEFT', num) + \
        permutations_removing_end_digit('RIGHT', num)
    permutations = set(permutations)

    for permute in permutations:
        if sieve.is_prime(int(permute)) is False:
            return False

    return True


if __name__ == '__main__':
    ''' Generate sieve and check for two way truncatable primes.
        Expect 11 values. '''

    trial_limit = 1000000
    sieve = PrimeSieve(trial_limit)
    sieve.generate()
    answer = []

    for i in range(8, trial_limit-1):
        if is_two_way_truncatable_prime(sieve, i) is True:
            answer.append(i)

    print answer
    print sum(answer)
    print len(answer)
