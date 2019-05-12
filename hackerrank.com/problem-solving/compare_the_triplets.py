# https://www.hackerrank.com/challenges/compare-the-triplets/problem

if __name__ == '__main__':
    a = tuple(map(int, input().split()))
    b = tuple(map(int, input().split()))
    d = list(map(lambda i: 1 if i[0] - i[1] > 0 else 0 if i[0] - i[1] == 0 else -1, zip(a, b)))
    print (d.count(1), d.count(-1))