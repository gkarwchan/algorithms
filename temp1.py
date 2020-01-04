n, m = map(int, input().split())
inputs = [input() for _ in range(n)]

d = { i: [] for i in range(n // 2, -1, -1)}
print ('--------------------------------')
for r, x in enumerate(inputs):
    segs = x.split('B')
    print (x)
    c = 0
    for y in segs:
        if len(y) > 0:
            d[min(r - 0, n - r)].append((r, c, len(y)))
        c += len(y) + 1
    d[min(r - 0, n - r)] = sorted(d[min(r - 0, n - r)], key = lambda x: x[2], reverse=True)
print (d)

# v = [(min(i - 0, n - i), i,  x.split('B')) for i, x in enumerate(inputs)]
# print (d)
