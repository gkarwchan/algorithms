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
Then we need to go through a loop from 2 to N and check if it is prime.  
But it turned out there is a more efficient way to do it.  


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
And we don't need to iterate over every number, as we can skip even values:  


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

if __name__ == '__main__':
    primecache = [2,3]
    for _ in range(int(input())):
      print(get_primes(int(input()), primelist))
```

The most successful so far

 from math import ceil, sqrt

def get_primes(n, primelist):
    primes = sum(primelist)
    if n <= primelist[-1]:
        return sum(i for i in primelist if i <= n)
    for candidate in range(primelist[-1] + 2, n + 1,2):
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
            primes += candidate
    return primes

if __name__ == '__main__':
    primelist = [2,3]
    for _ in range(int(input())):
      print(get_primes(int(input()), primelist))



Another and the fastest algorithm is (Sieve of Eratosthenes)[https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes] which will take out the non-prime numbers

from math import ceil, sqrt

def get_primes(n, primelist):

    a = [i for i in range(n+1)]

    for i in range(2,ceil(sqrt(n)) + 1):
        if a[i]:
            for j in range(i**2, n+1, i):
                a[j] = 0

    return sum(a) - 1

if __name__ == '__main__':
    primelist = [2,3]
    for _ in range(int(input())):
      print(get_primes(int(input()), primelist))


from math import ceil, sqrt

def get_primes(n, primelist):

    a = [i for i in range(n+1)]

    for i in range(2,ceil(sqrt(n)) + 1):
        if a[i]:
            a[i*i:n+1:i] = [0] * len(range(i*i, n+1, i))
            

    return sum(a) - 1

if __name__ == '__main__':
    primelist = [2,3]
    for _ in range(int(input())):
      print(get_primes(int(input()), primelist))







from math import ceil, sqrt

def get_primes(n, primelist, tot):
    
    if n <= primelist[-1]:
        return sum(i for i in primelist if i <= n)
    for candidate in range(primelist[-1] + 2, n + 1,2):
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
            tot[0] += candidate
    return tot[0]

if __name__ == '__main__':
    primelist = [2,3]
    tot = [5]
    for _ in range(int(input())):
      print(get_primes(int(input()), primelist, tot))







from math import ceil, sqrt

def get_primes():
    n = 10**2
    a = [i for i in range(2,n+1)]
    b = [0] * (n + 1)
    count = 0
    for i in range(2,ceil(sqrt(n)) + 1):
        if a[i]:
            count += a[i]
            a[i*i:n+1:i] = [0] * len(range(i*i, n+1, i))
        b[i] = count
            

    return b

if __name__ == '__main__':
    primelist = get_primes()
    print(primelist)
    # for _ in range(int(input())):
    #     print(get_primes(int(input()), primelist))





