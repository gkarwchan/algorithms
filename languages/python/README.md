# Iterators and iterables

According to Python documentation, an iterable is:  

> An object capable of returning its memebers one at a time.

Examples of iterables:  

* All sequence types: (list, str, tuple)
* Non-sequence types: (dict, file)
* Any object that implements: `__iter__()` or `__getitem__()` method.

When an iterable is passed to the built-in function `iter()`, it returns an iterator for the object.

Python gives us the ability to iterate of iterables, using a type of object called `iterator`. According to the official documentation:

> An iterator is an object representing a stream of data. Repeated calls to the iterator's `__next__` method return successive items in the stream.  

Iterator methods:  

1. `__next__()` instance method.
2. built-in function `next()` passing the iterator.
3. `StopIteration` is an exception raised when there is no more data.

## Iterating over multiple sequences

```python
people = ['John', 'Mike', 'David', 'Jacob']
ages = [34, 13, 87, 13]

for position, person in enumerate(people):
  age = ages[position]
  print(person, age)
```

Another Pythonic code:  

```python
people = ['John', 'Mike', 'David', 'Jacob']
ages = [34, 13, 87, 13]

for person, age in zip(people, ages):
  print (person, age)
```

## Comprehension

```python
[n ** 2 for n in range(10)]

[n ** 2 for n in range(10) if not n % 2]
```

#### Nested comprehension

```
[ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ] 
```
Requirements: Generate from 'ABCDE' all possible pairs:  
[('A', 'A'), ('A', 'B'), ('A', 'C'), ... 
 ('B', 'B'), ...
 ('C', 'C') ...]

```python
items = 'ABCDE'
pairs = []
for a in range(len(items)):
  for b in range(a, len(items)):
    pairs.append((item[a], items[b]))
```
In a list comprehension way:

```python
items = 'ABCDE'
pairs = [(items[a], items[b]) for a in range((len(items)) for b in range(a, len(items)))]
```

#### Filtering Comprehension

```python
from math import sqrt
mx = 10
legs = [(a, b, sqrt(a**2, b**2)) for a in range(1, mx) for b in range (a, mx)]
legs = list(filter(lambda triple: triple[2].is_integer(), legs))
```

Will be:

```python
from math import sqrt
mx = 10
legs = [(a, b, sqrt(a**2, b**2)) for a in range(1, mx) for b in range (a, mx)]

legs = [(a, b, int(c)) for a, b, c in legs if c.is_integer()]
```

Example:

One input array: 
data = [24, 35, 66, 34, 63]
frequency = [4, 3, 2, 1, 5]

output = [24, 24, 24, 24, 35, 35, 35, 66, 66, 34, 63, 63, 63, 63, 63]

```python
[y for x in zip(data, freq) for y in [x[0]] * x[1]]
```

## reduce

```python
from functools import reduce

reduce(lambda: x, y: x+y, ar)