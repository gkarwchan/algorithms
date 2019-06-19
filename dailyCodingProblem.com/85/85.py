def findNumber(x, y, b):
  return (x * b) + (y - ( b * y))

if __name__ == '__main__':
  x, y, b = map(int, input("enter x, y, z: ").split())
  print(findNumber(x, y, b))