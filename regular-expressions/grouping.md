## Grouping:

By placing part of a regular expression inside round brackets or parentheses, you can group that part of the regular expression together.  
There are two benefits for this:  

1. Deal with the entire group as one entity, so you can apply **`quantifier`** or **`alteration`**.
2. Using text matched by the capturing group with a process called `backreference`.

Examples of first case:

```js
Set(Value)? 
```

Matches either:  

1. "Set".
2. "SetValue".

For the second case, we are going to cover it in more details in section called `backreference`.


## Backreference:

Example of checking if a string has duplicate characters (Isogram):

```js
function isIsogram(str){ 
  return !/(\w).*\1/i.test(str)
}
```

## Backreference to failed group

There are two different 

## Task: IP address IPv4 and IPv6

```python
pv4 = r'(?:(?:25[0-5]|2[0-4][0-9]|[0-1]?\d{1,2})\.){3}(?:25[0-5]|2[0-4][0-9]|[0-1]?\d{1,2})'
pv6 = r'(?:[a-f\d]{1,4}:){7}[a-f\d]{4}'
pat = '^\\s*(?:({})|({}))\\s*$'.format(pv4, pv6)
n = int(input())
inputs = [input() for i in range(n)]

r = re.compile(pat)
for i in inputs:
  m = r.match(i)
  
  print ('Neither' if not m else 'IPv6' if m.group(2) else 'IPv4')
```