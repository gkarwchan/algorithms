# https://www.hackerrank.com/challenges/plus-minus/problem

from collections import Counter

'''
Elegant solution
Complexity: O(2n)
'''

def plusMinus(arr):
    v = Counter([i // ( abs(i) if i != 0 else 1) for i in arr])
    print ("{:.6f}".format(v[1] / len(arr)))
    print ("{:.6f}".format(v[-1] / len(arr)))
    print ("{:.6f}".format(v[0] / len(arr)))

'''
Brutal force solution
Complexity: O(n)
'''


def plusMinus1(arr):
    pos = neg = zero = 0
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zero += 1
    print ("{:.6f}".format(pos / len(arr)))
    print ("{:.6f}".format(neg / len(arr)))
    print ("{:.6f}".format(zero / len(arr)))



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    plusMinus(arr)
    

  
