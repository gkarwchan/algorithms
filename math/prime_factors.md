## the problem

Find all prime factors for a number N

## solution 1

the simple solution will be as follows:

```python

def prime_factors(n):
    p, num, s = 2, n, set()
    while p <= num:
        while num % p == 0:
            s.add(p)
            num //= p
        p += 1 if p == 2 else 2
    return s

```

## more mature solution

We don't have to do all numbers up the input number. We can just do up to the square of it, and then return the remaining

```python
def prime_factors(n):
    p, num, s = 2, n, set()
    while p <= ceil(sqrt(n)):
        while num % p == 0:
            s.add(p)
            num //= p
        p += 1 if p == 2 else 2
    if num > 2:
        s.add(num)
    return s
```


## For more games with prime factors

[Project Euler problem 3](project-euler.003.md)  
