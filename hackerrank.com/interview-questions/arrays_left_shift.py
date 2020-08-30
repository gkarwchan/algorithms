# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

def rotLeft(a, d):
  f = d % len(a)
  return ' '.join(a[f:] +a[:f])

if __name__ == '__main__':
    
    n,d = map(int, input().split())
    a = input().split()
    print (rotLeft(a,d))
