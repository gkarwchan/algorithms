
def get_primes():
    n = 10**6
    a = [i for i in range(n+1)]
    b = [0] * (n + 1)
    count = 0
    for i in range(2,n+1):
        if a[i]:
            count += a[i]
            a[i*i:n+1:i] = [0] * len(range(i*i, n+1, i))
        b[i] = count
            

    return b

if __name__ == '__main__':
    primelist = get_primes()
    for _ in range(int(input())):
        print(primelist[int(input())])

