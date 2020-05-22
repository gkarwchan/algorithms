# Primes

## Is Prime?

To find if a number is prime, we don't need to divided by all the number below it. Similar to [divisors](divisors.md) we need to only devided by number from 1 to the square root of N.  

### Python

```python
from math import ceil, sqrt

def isPrime(n):
    prime = True
    for i in range(2, ceil(sqrt(n)) + 1):
        if n % i == 0:
            prime = False
            break
    return prime
```


## Prime number generator

What if we want to list all prime numbers from 2 to N?.  
Then we need to go through a loop from 2 to N and check if it is prime.  
But it turned out there is a more effecient way to do it.  


### Python

```python
from math import ceil, sqrt

def get_primes(n):
    """get all primes from 2 to n"""
    primelist = []
    for candidate in range(2, n + 1):
        is_prime = True
        root = ceil(sqrt(candidate))
        for prime in primelist:
            if prime > root:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
    return primelist
```

