def catAndMouse(x, y, z):
  diff = abs(z-x) - abs(z -y)
  return 'Mouse C' if diff == 0 else 'Cat A' if diff < 0 else 'Cat B'

if __name__ == '__main__':
  q = int(input())
  
  for i in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])

    result = catAndMouse(x, y, z)
    print(result + '\n')