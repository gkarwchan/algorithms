# https://projecteuler.net/problem=9
# https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem

from math import floor, sqrt, ceil

"""
So to find a Pythagorean triplet (a, b, c) with a + b + c = s, we have to find a
divisor m (> 1) of s / 2
and an odd divisor k (= m + n) of s / 2m with m < k < 2m
and gcd(m, k) = 1. Then set n = k − m, d = s 2mk and plug these into (9.2).
A fairly simple implementation of that algorithm might look like
"""

def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a

def pythagorean_triplet(n):
    bvalue = lambda a, n: (n**2 - 2*n*a)//(2*n - 2*a)
    cvalue = lambda n, a, b: n - a - b
    ispythagorean = lambda a,b,c: (a**2 + b**2) == c**2
    triplets = [-1]
    for a in range(1,floor(n/3)+1):
        b = bvalue(a, n)
        c = cvalue(n, a, b)
        if ispythagorean(a, b, c):
            triplets.append(a*b*c)
    return max(triplets)


def pythagorean_triplet1(n):
    s2 = n // 2
    mlimit = ceil(sqrt(s2)) - 1
    triplets = [-1]
    for m in range(2, mlimit + 1):
        sm = s2 // m
        # reduce the search space by removing all factors 2
        while sm % 2 == 0:
            sm = sm // 2
        k = (m + 2) if m % 2 == 1 else (m + 1)
        while k < 2*m and k <= sm:
            if sm % k == 0 and gcd(k,m) = 1:
                d = s2 // (k*m)
                n = k - m
                a = d* (m**2 - n**2)
                b = 2 * d * m * n
                c = d * (m**2+n**2)
                triplets.append(a*b*c)
            k += 2
    return max(triplets)





if __name__ == '__main__':
    for _ in range(int(input())):
        print(pythagorean_triplet1(int(input())))
