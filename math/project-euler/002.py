# https://projecteuler.net/problem=2
# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

import doctest

def even_fibonacci(n):  
    """Return the sum of all fibonnaci sequence

    >>> even_fibonacci(10)
    10
    >>> even_fibonacci(100)
    44
    >>> even_fibonacci(15)
    10
    >>> even_fibonacci(2)
    2
    >>> even_fibonacci(34)
    44
    """
    first, second, sum = 0, 2, 0
    while second <= n:
        sum += second
        first, second = second, 4 * second + first
    return sum
        
if __name__ == '__main__':
    doctest.testmod()