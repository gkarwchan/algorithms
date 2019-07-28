# https://www.hackerrank.com/challenges/happy-ladybugs/problem


''' 
Without using any extra library
'''

def happyLadybugs(b):
  count = { i:b.count(i) for i in set(b) }
  if any(count[k] == 1 for k in count if k != '_'):
    return 'NO'
  if '_' in b:
    return 'YES'
  lastChar = None
  isSingle = False
  for i in b:
    if i != lastChar:
      if isSingle:
        return 'NO'
      isSingle = True
      lastChar = i
    else:
      isSingle = False
  return 'NO' if isSingle else 'YES'

'''
with using collections.Counter which is enhanced for performance
'''

from collections import Counter

def happyLadybugs1(b):
  count = Counter(b)
  if any(count[k] == 1 for k in count if k != '_'):
      return 'NO'
  return 'NO' if '_' not in b and any (b[i] != b[i - 1] and b[i] != b[i + 1] for i in range(1, n - 1)) else 'YES'


if __name__ == '__main__':
    g = int(input())
    for _ in range(g):
      n = int(input())
      d = input().strip()
      print(happyLadybugs(d))
