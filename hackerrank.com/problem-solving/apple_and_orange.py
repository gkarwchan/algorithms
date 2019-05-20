# https://www.hackerrank.com/challenges/apple-and-orange/problem

def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum([1 for app in apples if t >= a + app >= s]))
    print(sum([1 for org in oranges if t >= b + org >= s]))

def countApplesAndOranges2(s, t, a, b, apples, oranges):
    print(sum(t >= a + app >= s for app in apples))
    print(sum(t >= b + app >= s for app in oranges))

if __name__ == '__main__':
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    n, m = map(int, input().split())
    apples = list(map(int, input().split()))
    oranges = list(map(int, input().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
    

