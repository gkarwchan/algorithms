#!/bin/python3
# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

def breakingRecords(scores):
    minv = maxv = scores[0]
    maxv = scores[0]
    minBreak = maxBreak = 0
    for i in scores:
        if i > maxv:
            maxv = i
            maxBreak = maxBreak + 1
        elif i < minv:
            minv = i
            minBreak = minBreak + 1
    return [maxBreak, minBreak]


if __name__ == '__main__':
    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(*result)