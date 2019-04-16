if __name__ == '__main__':
  arr = [[input(), float(input())] for _ in range(int(input()))]
  secondHighest = sorted(list(set([mark for name, mark in arr])))[1]
  print('\n'.join(sorted([name for name, mark in arr if mark == secondHighest])))
