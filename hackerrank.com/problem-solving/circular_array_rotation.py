# web location
# https://www.hackerrank.com/challenges/circular-array-rotation/problem


def circularArrayRotation(a, k, queries):
    return [a[(val - k) % len(a)] for val in queries]

if __name__ == '__main__':
    n, k, q = map(int, input().split())
    arr = list(map(int, input().split()))
    queries = [int(input()) for _ in range(q)]
    result = circularArrayRotation(arr, k, queries)
    print('\n'.join(map(str, result)))