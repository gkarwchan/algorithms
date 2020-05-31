from math import sqrt, ceil
import doctest

def prime_factors(n):
    """Returns the Largest prime factor

    >>> prime_factors(10)
    5
    >>> prime_factors(17)
    17
    >>> prime_factors(13195)
    29
    """
    p, num, s = 2, n, set()
    while p <= ceil(sqrt(n)):
        while num % p == 0:
            s.add(p)
            num //= p
        p += 1 if p == 2 else 2
    if num > 2:
        s.add(num)
    return max(s)

if __name__ == '__main__':
    doctest.testmod()
    # for _ in range(int(input())):
    #     n = int(input())
    #     print(prime_factors(n))