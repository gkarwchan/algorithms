from math import ceil, sqrt

def get_primes(n):
    """get all primes from 2 to n"""
    primelist = []
    primes = 0
    for candidate in range(2, n + 1):
        is_prime = True
        root = ceil(sqrt(candidate))
        for prime in primelist:
            if prime > root:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        if is_prime:
            primelist.append(candidate)
            primes += candidate
    return primes

if __name__ == '__main__':
    for _ in range(int(input())):
      print(get_primes(int(input())))