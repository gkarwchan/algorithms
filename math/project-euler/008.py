# https://projecteuler.net/problem=8
# https://www.hackerrank.com/contests/projecteuler/challenges/euler008/problem

from collections import deque
from functools import reduce
from operator import mul

def findmaxprod(n, k):
    q = deque()
    maxprod = 1
    for i, c in enumerate(n):
        q.append(int(c))
        if i < k:
            maxprod *= int(c)
            continue
        q.popleft()
        maxprod = max(maxprod, reduce(mul, q, 1))
    return maxprod

if __name__ == '__main__':
    for _ in range(int(input())):
        n, k = map(int, input().split())
        nstring = input()
        print(findmaxprod(nstring, k))

