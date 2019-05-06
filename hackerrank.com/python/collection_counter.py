# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

if __name__ == '__main__':
    x = int(input())
    sizes = Counter(list(map(int, input().split())))
    n = int(input())
    customers = [list(map(int, input().split())) for _ in range(n)]
    money = 0
    for size, pay in customers:
        if size in sizes and sizes[size] > 0:
            money += pay
            sizes[size] -= 1
    print (money)

    
    