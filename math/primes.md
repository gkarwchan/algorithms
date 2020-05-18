# Primes

## Is Prime?

To find if a number is prime, we don't need to divided by all the number below it. Similar to [divisors](divisors.md) we need to only devided by number from 1 to:  

$$n = x^{l + 1} - x^l$$

# Python

```python
from math import floor, sqrt

def primes(n):
```