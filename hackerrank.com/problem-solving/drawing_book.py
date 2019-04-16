def pageCount(n, p):
  begining = p // 2
  end = n // 2 - p // 2
  return min(end, begining)
