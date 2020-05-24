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

