#!/usr/bin/python
'''
Project Euler
Problem 35
'''


class PrimeSieve:
    ''' Implementation of Sieve of Eratosthenes.
        See .generate() for sieve logic.
        Not optimised.
    '''

    def __init__(self, limit):
        ''' Set sieve limit and mark as unprocessed. '''
        self.limit = limit
        self.generated = False

    def generate(self):
        ''' Populate sieve with non prime values. '''
        self.sieve = set()
        for x in range(2, self.limit+1):
            if x not in self.sieve:
                self.sieve.update(range(x*x, self.limit+1, x))
        self.generated = True

    def is_prime(self, num):
        ''' Test if number is prime by not appearing in the sieve. '''
        assert self.generated, 'Run GENERATE before checking primality.'
        if num is 1:
            return False
        if num in self.sieve:
            return False
        return True

    def get_primes(self):
        ''' Return all primes within limit. '''
        assert self.generated, 'Run GENERATE before fetching primes.'

        # range 2-limit minus non prime set gives primes
        primes = set(range(2, self.limit)) - self.sieve
        return primes

    def rotate(self, num):
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
        number_list = self.rotate(num)
        for permutation in number_list:
            if self.is_prime(permutation) is False:
                return False
        return True


if __name__ == "__main__":
    '''
    Count the circular primes under 1'000'000.
    '''

    sieve = PrimeSieve(1000000)
    sieve.generate()
    print sieve.get_primes()
