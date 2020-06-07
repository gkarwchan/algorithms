# https://projecteuler.net/problem=9
# https://www.hackerrank.com/contests/projecteuler/challenges/euler009/problem

from math import floor

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



if __name__ == '__main__':
    for _ in range(int(input())):
        print(pythagorean_triplet(int(input())))
