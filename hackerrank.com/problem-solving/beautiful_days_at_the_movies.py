def beautifulDays(i, j, k):
    return sum ([1 for i in range(i, j + 1) if (int(str(i)[::-1]) - i) % k == 0])
