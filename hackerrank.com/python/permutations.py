# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

if __name__ == '__main__':
      s, k = input().split()
      k = int(k)
      result = sorted(list(map(lambda x: ''.join(x), permutations(s, k))))
      print ('\n'.join(result))
      
      
