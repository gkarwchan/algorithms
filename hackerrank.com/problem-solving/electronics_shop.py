# https://www.hackerrank.com/challenges/electronics-shop/problem
'''
Pythonic way: one line
But it is the slowest: O(n^2)
'''
def getMoneySpent(keyboards, drives, b):
  return max([k + d for k in keyboards for d in drives if b >= k + d], default = -1)


'''
Second attempt: faster in some condition
O(n * m) modified
The same as above, but in case there is no enough money,
no need to go through all the loop, and exit immediateley 
'''

def getMoneySpent3(keyboards, drives, b):
  keyboards.sort(reverse = True)
  drives.sort(reverse = True)
  if keyboards[-1] + drives[-1] > b:
    return -1
  if keyboards[0] + drives[0] <= b:
    return keyboards[0] + drives[0]
  amount = 0
  for drive in drives:
    for keyboard in keyboards:
      cost = drive + keyboard
      if cost == b:
        return b
      elif cost < b:
        amount = max(cost, amount)
        break
  return amount

