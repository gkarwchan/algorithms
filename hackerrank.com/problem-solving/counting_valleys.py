# https://www.hackerrank.com/challenges/counting-valleys/problem

from collections import Counter

from itertools import accumulate
from functools import reduce

def countingValleys(n, s):
    a = map(lambda i: 1 if i == 'U' else -1, s)
    b = accumulate(a)
    vc = reduce(lambda acc, i: (i, acc[1] + 1) if acc[0] == -1 and i == 0 else (i, acc[1]), b, (0, 0))
    return vc[1]

    
    
    
        
if __name__ == '__main__':
    n = int(input())
    
    ar = input()
    print(countingValleys(n, ar))

    

