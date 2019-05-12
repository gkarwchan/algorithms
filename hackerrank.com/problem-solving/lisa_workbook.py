# https://www.hackerrank.com/challenges/lisa-workbook/problem

'''
short version
'''

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = [int(i) for i in input().split()]
    a = [i[j:j+k] for i in map(lambda i: [*iter(range(1, i + 1))], arr) for j in range(0, len(i), k)]
    print (sum([1 for i in range(len(a)) if i + 1 in a[i]]))

'''
more descriptive version
'''

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = [int(i) for i in input().split()]
    abc = []
    for i in arr:
        inputs = list(range(1, i + 1))
        abc.extend([inputs[j:j+k] for j in range(0, i, k)])
    print (sum([1 for i in range(len(abc)) if i + 1 in abc[i]]))
