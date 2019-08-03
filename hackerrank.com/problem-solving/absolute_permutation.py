# https://www.hackerrank.com/challenges/absolute-permutation/problem

def absolutePermutation(n, k):
  if k == 0:
    return ' '.join([str(i) for i in range(1, n + 1)])
  if n % (2 * k) > 0:
    return '-1'
  spots = [0] * n
  for i in range(n):
    cycle = int(i/2/k)
    innerIndex = i % (2 * k)
    innerCycle = int(innerIndex / k)
    innerCycleReverse = 1 if innerCycle == 0 else 0
    spots[i] = (cycle * 2 * k) + ((i % k) + 1) + (k * innerCycleReverse)
  
  return ' '.join([str(i) for i in spots])

  


if __name__ == '__main__':
  t = int(input())
  inputs = [list(map(int, input().split())) for _ in range(t)]
  
  outputs = [absolutePermutation(i[0], i[1]) for i in inputs]
  print('\n'.join(outputs))
