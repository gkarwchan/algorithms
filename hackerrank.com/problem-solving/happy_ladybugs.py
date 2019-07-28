# https://www.hackerrank.com/challenges/happy-ladybugs/problem

def happyLadybugs(b):
  blist = list(b)
  count = { i:blist.count(i) for i in set(blist) }
  for k, v in count.items():
    if v == 1 and k != '_':
      return 'NO'
  if '_' in blist:
    return 'YES'
  lastChar = None
  isSingle = False
  for i in blist:
    if i != lastChar:
      if isSingle:
        return 'NO'
      isSingle = True
      lastChar = i
    else:
      isSingle = False
  return 'YES'


if __name__ == '__main__':
    g = int(input())
    for _ in range(g):
      n = int(input())
      d = input().strip()
      print(happyLadybugs(d))
