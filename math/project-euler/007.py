# https://projecteuler.net/problem=7
# https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem

def primaryat(n, cache=[2,3]):
    if len(cache) >= n:
        return cache[n-1]
    else:
        num = cache[-1]
        while len(cache) < n:
            num += 2
            isPrime = True
            for d in cache:
                if num % d == 0:
                    isPrime = False
                    break
            if isPrime:
                cache.append(num)
        return cache[n-1]


if __name__ == '__main__':
    for _ in range(int(input())):
        print(primayat(int(input())))