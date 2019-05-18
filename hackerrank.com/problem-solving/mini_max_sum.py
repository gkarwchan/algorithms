#  https://www.hackerrank.com/challenges/mini-max-sum/problem

def miniMaxSum(arr):
  ar = sorted(arr)
  print(sum(ar[0:4]), sum(ar[1:5]))


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    miniMaxSum(arr)