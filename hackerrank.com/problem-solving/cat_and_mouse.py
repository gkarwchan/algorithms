# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

def catAndMouse(x, y, z):
  diff = abs(z-x) - abs(z -y)
  return 'Mouse C' if diff == 0 else 'Cat A' if diff < 0 else 'Cat B'

if __name__ == '__main__':
  q = int(input())
  
  for i in range(q):
    x, y, z = map(int, input().split())
    print(catAndMouse(x, y, z) + '\n')
    