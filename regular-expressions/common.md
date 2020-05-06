## IP Address Validation
This code will validate if the entry is IPv4, IPv6 or not an IP

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

## Email Address:

For simplicity we do like this

```python
exp = r'\b[\w.]+@\w+(?:\.[a-zA-Z]{2,})*\b'
```
## Domain Names:

```python
exp = r'\bhttps?:\/\/(?:www\.|ww2\.)?((?:[\w-]+\.){1,}\w+)\b'
```
