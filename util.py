#!/usr/bin/python
'''
Project Euler
Utility module
'''


def pandigital(n, number):
    """ Test number is pandigital to nth degree. """
    assert type(n) is int, "n should be integer"
    assert type(number) is int, "number should be integer"
    assert n > 0, "n should be positive."

    number = str(number)
    if len(number) != n:
        return False
    for x in range(1,n):
        if not x in number:
            return False
    return True


class PrimeSieve:
    ''' Implementation of Sieve of Eratosthenes.
        See .generate() for sieve logic.
        
        Sieve unoptimised.
        Optimised to drop sieve after generating primes in favour of a set
        of primes.
    '''

    def __init__(self, limit):
        ''' Set sieve limit and mark as unprocessed. '''
        self.limit = limit
        self.generated = False

    def generate(self):
        ''' Populate sieve with non prime values.
            Store primes and dump sieve.'''
        self.sieve = set()
        for x in range(2, self.limit+1):
            if x not in self.sieve:
                self.sieve.update(range(x*x, self.limit+1, x))
        self.primes = set(range(2,self.limit+1)) - self.sieve
        self.sieve = None
        self.generated = True

    def is_prime(self, num):
        ''' Test if passed number is a prime. '''
        assert self.generated, 'Run GENERATE before checking primality.'
        assert type(num) is int, 'Tested number is not an INTEGER.'
        assert num < self.limit, 'Tested number (%d) exceeds defined prime limit(%d).' % (int(num), int(self.limit))
        #assert num > 0, 'Tested number (%d) is less that 1.' % (num)
        if num in self.primes:
            return True
        return False

    def get_primes(self):
        ''' Return list of all primes within limit. '''
        return list(self.primes)

    @classmethod
    def rotate_number(cls, num):
        ''' Permutate the number by cycling the digits
            eg.
                123 : 123
                      231
                      312
        '''
        # Split the number to a list
        lst_num = [int(x) for x in str(num)]
        # seed permutations with original number
        permutations = [num]
        # for length of number -1 move the leading digit to the end.
        for x in range(1, len(lst_num)):
            lst_num = lst_num[1:]+ [lst_num[0]]
            permute = int(''.join([str(y) for y in lst_num]))
            permutations.append(permute)

        # return list of rotated permutations
        return permutations

    def are_all_circular_permutations_prime(self, num):
        '''
        Given a number, test all circular permutations for
        primality and return true if all succeed.
        '''
        number_list = self.rotate_number(num)
        for permutation in number_list:
            if self.is_prime(permutation) is False:
                return False
        return True

if __name__ == '__main__':
    sieve = PrimeSieve(100)
    sieve.generate()
    print sieve.get_primes()
