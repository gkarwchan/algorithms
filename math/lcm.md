# Least Common Multiple (LCM)
The least common multiple (LCM) of two numbers is the smallest positive integer that is perfectly divisible by the two given numbers.

# Python

```python

def lcm(x, y):
  greater = max(x, y)
  while True:
    if greater % x == 0 and greater % y == 0:
      return greater
    greater += 1
  return 0 

```
Or using GCD:

```matlab
lcm (x, y) = (x * y) // gcd(x, y)
```

## LCM for multi numbers

```matlab
lcm(x,y,z) = lcm(x, lcm(y,z))
```
Using Python

```python
def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a

def lcm(a, b, *rest):
    # print ('input: ', a, b, rest)
    rslt = (a*b) // gcd(a, b)
    if rest:
        return lcm(rslt, rest[0], *rest[1:])
    else:
        return rslt
        
```
