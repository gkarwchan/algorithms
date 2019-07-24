# https://www.hackerrank.com/challenges/the-grid-search/problem


def gridSearch(G, P):
  rowRange = len(G) - len(P) + 1
  colRange = len(G[0]) - len(P[0]) + 1
  result = 'NO'
  
  for i in range(rowRange):
    beg = 0
    while beg <= colRange:
      pos = G[i].find(P[0], beg)
      if pos == -1:
        break
      beg = pos + 1
      result = 'YES'
      for k in range(len(P)):
        if G[i + k][pos:pos+len(P[0])] != P[k]:
          result = 'NO'
          break
      if result == 'YES':
          break
    if result == 'YES':
      break


  return result


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
      R, C = map(int, input().split())
      G = [input() for _ in range(R)]
      r, c = map(int, input().split())
      P = [input() for _ in range(r)]
      result = gridSearch(G, P)
      print(result)
