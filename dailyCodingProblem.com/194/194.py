def intersectingPairs(p, q):
  n = len(p)
  count = 0
  for i in range(n):
    for j in range(i+1, n):
      if (p[i] - p[j]) * (q[i] * q[j]) < 0:
        count += 1
  return count
