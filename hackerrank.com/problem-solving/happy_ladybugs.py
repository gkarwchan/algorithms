# https://www.hackerrank.com/challenges/happy-ladybugs/problem

def happyLadybugs(b):
  count = { i:b.count(i) for i in set(b) }
  for k, v in count.items():
    if v == 1 and k != '_':
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


if __name__ == '__main__':
    g = int(input())
    for _ in range(g):
      n = int(input())
      d = input().strip()
      print(happyLadybugs(d))
