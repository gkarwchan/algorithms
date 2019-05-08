# Web location
# https://www.hackerrank.com/challenges/minimum-distances/problem

'''
Complexity: O(n)
'''

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    dictd = {}
    for i, val in enumerate(arr):
        if val in dictd:
            newDistance = i - dictd[val][0]
            dictd[val] = [
                i, 
                newDistance if dictd[val][1] == -1 else min(newDistance, dictd[val][1])
            ]
        else:
            dictd[val] = [i, -1]
    dist = [val[1] for val in dictd.values() if val[1] > 0]
    if len(dist) == 0:
        print(-1)
    else:
        print(min(dist))