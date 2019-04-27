from math import sqrt

def standardDiviation (arr):
    mean = sum(arr) / len(arr)
    return sqrt(sum(list(map(lambda val:  (mean - val) ** 2, arr))) / len(arr))

if __name__ == '__main__':
    count = int(input())
    values = list(map(int, input().rstrip().split()))

    variance = standardDiviation(values)
    print ('{:.1f}'.format(variance))