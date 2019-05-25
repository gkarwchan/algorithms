# Least Common Multiple (LCM)
The least common multiple (LCM) of two numbers is the smallest positive integer that is perfectly divisible by the two given numbers.

# Python

```python

def lcm(x, y):
  greater = max(x, y)
  while True:
    if greater % x == 0 and greater % y == 0:
      return greater
      break
    greater += 1
  return 0 

  ```
Or using GCD:

```matlab
lcm (x, y) = (x * y) // gcd(x, y)
```
