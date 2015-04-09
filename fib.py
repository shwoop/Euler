#!/usr/bin/python
'''
Fibonacci solutions

Multiple solutions to generating a fibonacci sequence.
Investigation following brain fart during interview.
No use of google/docs/stack.


TODO: Tests should return sets rather than print so they can be profiled.


ADVICE: just use fib_get() if importing externally.
'''


def fib_gen():
    ''' Generator solution to fib problem. '''

    # Seed initial values of first,second with 1,1
    first = 1
    second = 1

    # yield initial 1,1 of sequence
    yield first
    yield second

    # loop ad infinitum generating next fib value and updating first,second
    while True:
        result = first + second
        first, second = second, result
        yield result


def fib_gen_solution(num):
    ''' Trial generator solution. '''
    fg = fib_gen()
    for i in range(1, num):
        print next(fg)


def fib_rec(it_target, first=1, second=1, it_cnt=2):
    ''' Recursive solution to fib problem. '''
    # it_cnt is seeded to 2 to account for the two seeded 1 values.
    if it_target in range(1, 3):
        return 1

    tmp = first + second
    it_cnt = it_cnt + 1

    if it_cnt == it_target:
        return tmp
    else:
        first, second = second, tmp
        return fib_rec(it_target, first, second, it_cnt)


def fib_rec_solution(num):
    ''' Trial recursive solution. '''
    for n in range(1, num):
        print fib_rec(n)


def fib_imp(iterations):
    ''' Imperativly get fib sequence. '''
    sequence = [1,1]

    # edge cases
    if iterations is 1:
        return [1]
    if iterations is 2:
        return sequence

    for i in range(2, iterations-1):
        nxt = sequence[i-1] + sequence[i-2]
        sequence.append(nxt)

    return sequence


def fib_imp_solution(num):
    ''' Trial imperative solution. '''
    for x in fib_imp(num):
        print x


class FibIterator:
    ''' Class based iterator solution to fibonnacci issue. '''

    def __init__(self):
        ''' Seed sequence with 1,1 and set count to 0. '''
        self._n_minus_1 = 1
        self._n_minus_2 = 1
        self._cnt = 0

    def __iter__(self):
        ''' Return iterator object. '''
        return self

    def next(self):
        ''' update n-1 and n-2 values as well as count of iterations. ''' 
        # Not too elegant
        self._cnt = self._cnt + 1
        if self._cnt in [1,2]:
            return 1

        # Calculate next value, update previous 2 and return
        nxt = self._n_minus_2 + self._n_minus_1
        self._n_minus_2, self._n_minus_1 = self._n_minus_1, nxt

        return nxt


def fib_class_solution(num):
    ''' Trial class based iterator solution. '''
    fi = FibIterator()
    for x in range(0, num):
        print next(fi)


if __name__ == '__main__':
    ''' Entry point.  Uncomment to test a solution. '''
    TST_RANGE = 10

    print '\r\n\tGENERATOR RESULTS.'
    fib_gen_solution(TST_RANGE)

    print '\r\n\tRECURSIVE RESULTS.'
    fib_rec_solution(TST_RANGE)

    print '\r\n\tIMPERATIVE RESULTS.'
    fib_imp_solution(TST_RANGE)

    print '\r\n\tITERATOR RESULTS.'
    fib_class_solution(TST_RANGE)
