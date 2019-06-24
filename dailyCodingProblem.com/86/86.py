def findMinimum(x):
  numeric = [1 if i == '(' else -1 for i in x]
  return abs(sum(numeric))

if __name__ == '__main__':
  x = input('Input the parentheses value: ')
  print(findMinimum(x))