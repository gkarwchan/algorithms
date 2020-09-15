# https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements/0

def rotateArray(n, array):
    if (len(array) == 0): return array
    limit = n % len(array)
    return array[limit:] + array[:limit]

if __name__ == '__main__':
    T = int(input())
    inputs = [( tuple(map(int, input().split())), list(map(int, input().split()))) for _ in range(T)]
    outputs = [rotateArray(x[0][1], x[1]) for x in inputs]
    v = [' '.join('{0}'.format(y) for y in x) for x in outputs]
    print ('\n'.join(v))
