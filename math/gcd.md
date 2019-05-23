# Greatest Common Factor (GCD)

the GCD also called Highest Common Factor (HCF) is the largest positive integer that devides each of many integers.

24 = __2__ * 2 * 2 * __3__  
18 = __2 * 3__ * 3


# Python

```python
def gcdCalc(a, b):
  if (b == 0):
    return a
  else:
    return gcdCalc(b, a%b)

if __name__ == '__main__':
  print(gcdCalc(24, 36))
  
```