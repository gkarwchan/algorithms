# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

if __name__ == '__main__':
      s, k = input().split()
      result = [''.join(j) for i in range(1, int(k) + 1) for j in combinations(sorted(s), i)]
      print ('\n'.join(result))