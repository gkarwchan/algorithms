# All divisors
To find all divisors of a natural number, we need to do a loop, but that loop doesn't have to be for the whole number, but from the root square of the number:

```python
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
```