# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem


'''
complicated but fast O(n)
'''

def divisibleSumPairs(n, k, ar):
    res = [0] * k
    for i in ar:
        res[i % k] += 1
    acc = 0
    for i in range(1, (k - 1) // 2 + 1):
        acc += res[i] * res[k - i]
    selfSum = [0, k // 2] if k % 2 == 0 else [0]
    for i in selfSum:
        acc += res[i] * (res[i] - 1) // 2
    return acc

'''
simpler but O(n**2)        
'''

def divisibleSumPairs1(n, k, ar):
    count = 0
    for i in range(0, n - 1):
        for j in range (i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                count = count + 1
    return count

'''
or pythonic code
'''

def divisibleSumPairs2(n, k, ar):
    return sum(1 for i in range(n - 1) for j in range(i + 1, n) if (a[i] + a[j]) % k == 0)



if __name__ == '__main__':
    n, k = map(int, input().split())
    ar = list(map(int, input().split()))
    print(divisibleSumPairs(n, k, ar))

    

