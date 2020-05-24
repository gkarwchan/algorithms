## Solution 1

This is a naive implementation. The cost of it is O(n^2)

```python

def fibonicci(n):
  if n in [1,2]
    return n
  else:
    return fibonicci(n - 2) + fibonicci(n - 1)

if __name__ == '__main__':         
    assert fibonacci(9) == 55
    assert fibonacci(10) == 89
    assert fibonacci(11) == 144
    assert fibonacci(1) == 1
    assert fibonacci(2) == 2
    print('good algo')
```

To look at the performance try this:

```bash
python3 -m cProfile fibonicci.py
```
## Solution 2

In order to enhance the performance we add a cache as follows:

```python
def fibonacci(n):  
    cache = [1,1] + [0] * (n - 1)
    if cache[n] > 0:
        return cache[n]
    else:
        cache[n - 2] = fibonacci(n - 2)
        cache[n - 1] = fibonacci(n - 1)
        return cache[n - 2] + cache[n - 1]
```

## Solution 3
Another approach with O(n)

```python
def fibonacci(n):  
    first = 1
    second = 2
    if (n <= 2):
        return n
    else:
        strt = 3
        while strt <= n:
            first, second = second, first
            second += first
            strt += 1
        return second

```

## For more related to Fibonacci check these:

[project Euler problem 2](project-euler/002.md)  