# Web location
# https://www.hackerrank.com/challenges/halloween-sale/problem


if __name__ == '__main__':
    p, d, m, s = map(int, input().split())
    counter = 0
    while s >= p:
        counter += 1
        s -= p
        p = p - d if p - d >= m else m
    print (counter)
    
