# https://projecteuler.net/problem=1
# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

import doctest 

def solution(n):
  """Returns the sum of all multiples of 3 and 5 below n.

  >>> solution(3)
  0
  >>> solution(600)
  83700
  """
  return sum (x for x in range(n) if not (x % 3 and x % 5))

if __name__ == '__main__':
  doctest.testmod()