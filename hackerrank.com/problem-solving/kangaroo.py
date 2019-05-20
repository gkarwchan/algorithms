# https://www.hackerrank.com/challenges/kangaroo/problem

def kangaroo(x1, v1, x2, v2):
    if v2 >= v1:
        return 'NO'
    rem = (x2 - x1) % (v1 - v2)
    return 'YES' if rem == 0 else 'NO'


if __name__ == '__main__':
    x1, v1, x2, v2 = map(int, input().split())

    print(kangaroo(x1, v1, x2, v2))
    