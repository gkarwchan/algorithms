# https://www.hackerrank.com/challenges/finding-the-percentage/problem

if __name__ == '__main__':
  dictionary = {}
  for _ in range(int(input())):
    name, *marks = input().split()
    dictionary[name] = list(map(float, marks))
  print("{:.2f}".format(sum(dictionary[input()]) / 3.0))
