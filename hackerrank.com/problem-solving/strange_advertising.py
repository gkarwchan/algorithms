def viralAdvertising(n):
    lastval = acm = 2
    for _ in range(1, n):
        lastval = lastval * 3 // 2
        acm += lastval
    return acm

if __name__ == '__main__':
    n = int(input())
    result = viralAdvertising(n)
    print(result)
    