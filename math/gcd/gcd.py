def gcdCalc(a, b):
  if (b == 0):
    return a
  else:
    return gcdCalc(b, a%b)