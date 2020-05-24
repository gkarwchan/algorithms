import math

def divisors (number):
  rslt = []
  for i in range(1, math.floor(math.sqrt(number)) + 1):
    if number % i == 0:
      rslt.append(i)
      if i != number // i:
        rslt.append(number // i)
  rslt.sort()
  return rslt

def gcdCalc(a, b):
  if (b == 0):
    return a
  else:
    return gcdCalc(b, a%b)

def fibonacci(n):  
    first = 1
    second = 2
    if (n <= 2):
        return n
    else:
        strt = 3
        while strt <= n:
            first, second = second, first
            second += first
            strt += 1
        return second

