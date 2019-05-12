# https://www.hackerrank.com/challenges/flatland-space-stations/problem

'''
complexity: O(n)
'''

from math import ceil
def flatlandSpaceStations(n, c):
    c.sort()
    dist = [c[0]] + [ceil((c[i] - c[i - 1] - 1) / 2) for i in range(1, len(c))] + [n - 1 - c[-1]]
    return max(dist)


if __name__ == '__main__':
    n, m = map(int, input().split())
    c = list(map(int, input().split()))

    print (flatlandSpaceStations(n, c))
    
