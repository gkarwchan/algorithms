import os
import sys


def getMoneySpent(keyboards, drives, b):
  return max([k + d for k in keyboards for d in drives if b >= k + d], default = -1)
  

if __name__ == '__main__':
    

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent))

