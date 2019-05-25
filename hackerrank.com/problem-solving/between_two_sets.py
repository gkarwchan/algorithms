# https://www.hackerrank.com/challenges/between-two-sets/problem

from functools import reduce

def gcd(a, b):
  if (b == 0):
    return a
  else:
    return gcd(b, a%b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

def getTotalX(a, b):
    lcm_a = reduce(lambda x, y: lcm(x, y), a)
    gcd_b = reduce(lambda x, y: gcd(x, y), b)
    return sum([1 for i in range(1, (gcd_b // lcm_a) + 1) if gcd_b % (lcm_a * i) == 0])

    


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(getTotalX(a, b))

    

