# Naive implemenation
def calc_set_bits(n):
  c = 0
  for i in range(n):
      b = "{0:b}".format(i+1)
      c += b.count('1')
  return c


# complex implementation
import math
def calc_set_bits_complex(n):
    v = [1,2,4,5,7,9,12,13,15,17,20]
    if n < 12:
        return v[n-1]
    x = math.floor(math.log2(n))
    return int(x * math.pow(2, x -1) + (n - math.pow(2,x) + 1) + calc_set_bits_complex(int(n-math.pow(2, x))))