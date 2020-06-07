# Primes

## Is Prime?

To find if a number is prime, we don't need to divided by all the number below it. Similar to [divisors](divisors.md) we need to only divided by number from 1 to the square root of N.  

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
It turns out that the most effeciant way to do that is an algorithm called (Sieve of Eratosthenes)[https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes] which is very simple, and depends on pre-calculation. Before using this algorithm I will discuss other algorithgm.  

We don't need to go through a loop from 2 to N and check if it is prime, because we need to do up to the square root of the number only.  


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

To speed it up moreAnd we don't need to iterate over every number, as we can skip even values:  


```python
from math import ceil, sqrt

def get_primes(n):
    """get all primes from 2 to n"""
    primelist = [2]
    for candidate in range(3, n + 1,2):
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

If we want to do it many times then we can create a cache:  

```python
from math import ceil, sqrt

def get_primes(n, primecache):
    if n <= primecache[-1]:
        return sum(i for i in primecache if i <= n)
    primes = sum(primecache)
    for candidate in range(primecache[-1] + 2, n + 1,2):
        is_prime = True
        root = ceil(sqrt(candidate))
        for prime in primecache:
            if prime > root:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primecache.append(candidate)
            primes += candidate
    return primes
```

## Sieve of Eratosthenes

By testing on the site HackerRank, the fastest algorithm is (Sieve of Eratosthenes)[https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes] which is very simple. for each prime numbers take out all its numbers that are multiplication of it. 


```python

def get_primes(n):
    a = [i for i in range(n+1)]
    for i in range(2,n+1):
        if a[i]:
            a[i*i:n+1:i] = [0] * len(range(i*i, n+1, i))
    return a
```

