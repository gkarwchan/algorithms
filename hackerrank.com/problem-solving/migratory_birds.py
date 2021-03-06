# https://www.hackerrank.com/challenges/migratory-birds/problem

def migratoryBirds(arr):
    count = {i: 0 for i in set(arr)}
    for i in arr:
        count[i] += 1
    sortedResult = sorted(count.items(), key=lambda x:(x[1], x[0]), reverse=True)
    return list(filter(lambda x: x[1] == sortedResult[0][1], sortedResult))[-1][0]

def migratoryBirds1(arr):
    count = [0] * 5
    for i in arr:
        count[i - 1] += 1
    return arr.index(max(arr)) + 1
    


if __name__ == '__main__':
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    print(migratoryBirds(ar))
