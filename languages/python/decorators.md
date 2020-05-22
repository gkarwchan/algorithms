# Decorators

It is best to describe it by an example. Let us build a time measurement.  


```python
from time import sleep, time

def f():
    sleep(.3)

def g():
    sleep(.5)

t = time()
f()
print ('f took: ', time() - t)

t = time()
g()
print ('g took: ', time() - t)

```


```python
from time import sleep, time

def f():
    sleep(.3)

def g():
    sleep(.5)

def measure(func):
    t = time()
    func()
    print(func.__name__, 'took: ', time() - t)

measure(f)
measure(g)
```

But what if we want to pass values to f, g.

```python
from time import sleep, time

def f(sleep_time = 0.1):
  sleep(sleep_time)

def measure(func):
  def wrapper(*args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took: ', time() - t)
  return wrapper


f = measure(f)

f(0.5)
f(sleep_time = 0.3)

```

```python
from time import sleep, time


def measure(func):
  def wrapper(*args, **kwargs):
    t = time()
    func(*args, **kwargs)
    print(func.__name__, 'took: ', time() - t)
  return wrapper

@measure
def f(sleep_time = 0.1):
  sleep(sleep_time)



f(0.5)
f(sleep_time = 0.3)
print(f.__name__)

```

what if the function return values:

```python
from time import sleep, time
from functools import wraps

def measure(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    t = time()
    result = func(*args, **kwargs)
    print(func.__name__, 'took: ', time() - t)
    return result
  return wrapper

@measure
def f(sleep_time = 0.1):
  """something for test"""
  sleep(sleep_time)



f(0.5)
f(sleep_time = 0.3)
print(f.__name__, f.__doc__)

```