# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

'''
My point is delete an element from list is better that doing nested loops
'''

def minimumBribes(arr):
    acc, ord = 0, list(range(1, len(arr) + 1))
    try:
        for i in range(len(arr) - 1):
            tup = (ord[0], ord[1], ord[2] if len(ord) > 2 else 0)
            pos = tup.index(arr[i])
            acc += pos
            del ord[pos]
    except ValueError:
        return "Too chaotic"        
    return  acc

if __name__ == '__main__':
    b = int(input())
    for i in range(b):
        input()
        print (minimumBribes(list(map(int, input().split()))))
        