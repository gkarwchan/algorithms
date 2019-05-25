# https://www.hackerrank.com/challenges/the-birthday-bar/problem
def birthday(s, d, m):
  return sum([1 for i in range(len(s) - m + 1) if sum(s[i:i + m]) == d])


if __name__ == '__main__':
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    d,m = map(int, input().split())
    result = birthday(s, d, m)
    print(result)
