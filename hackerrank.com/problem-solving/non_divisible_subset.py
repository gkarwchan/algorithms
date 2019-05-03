from math import ceil

if __name__ == '__main__':
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    counts = [[] for _ in range(k)]
    for i in ar:
        counts[i % k].append(i)
    maxCount = 0
    for i in range(1, ceil(k/2)):
        maxCount += max(len(counts[i]), len(counts[k - i]))
    if len(counts[0]) > 0:
        maxCount += 1
    if k % 2 == 0 and len(counts[k // 2]) > 0:
        maxCount += 1

    print (maxCount)
