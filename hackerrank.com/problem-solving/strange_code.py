# https://www.hackerrank.com/challenges/strange-code/problem

import math

def strangeCounter(t):
  rank = int(math.log((t + 2) / 3, 2))
  sumBefore = (math.pow(2, rank) - 1) * 3
  rankTop = math.pow(2, rank) * 3
  return int(rankTop - t + sumBefore + 1)


def strangeCounter1(t):
  rank = int(math.log((t -1) // 3+1, 2))
  sumBefore = (math.pow(2, rank) - 1) * 3
  rankTop = math.pow(2, rank) * 3
  return int(rankTop - t + sumBefore + 1)

if __name__ == '__main__':
  t = int(input())
  print(strangeCounter(t))

