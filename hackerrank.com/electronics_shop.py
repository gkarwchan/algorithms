import os
import sys


def getMoneySpent(keyboards, drives, b):
  keyboards.sort(reverse = True)
  drives.sort(reverse = True)
  if keyboards[-1] + drives[-1] > b:
    return -1
  k = amount = 0
  for drive in drives:
    while k < len(keyboards) and drive + keyboards[k] > b:
      k += 1
    if k == len(keyboards):
      k = 0
      continue
    cost = drive + keyboards[k]
    if cost == b:
      return b
    if cost > amount:
      amount = cost
    k = 0
  return amount

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

