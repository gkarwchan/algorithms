# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations

if __name__ == '__main__':
      s, k = input().split()
      result = sorted(list(map(lambda x: ''.join(x), permutations(s, int(k)))))
      print ('\n'.join(result))
      
      
