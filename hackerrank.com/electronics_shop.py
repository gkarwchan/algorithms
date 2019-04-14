

'''First attempt: clean.
we sort by descending, so there is a probability that it can be faster as we seek the higher to spend
'''

def getMoneySpent(keyboards, drives, b):
  keyboards.sort(reverse = True)
  drives.sort(reverse = True)
  amount = -1
  for drive in drives:
    for keyboard in keyboards:
      cost = drive + keyboard
      if cost == b:
        return b
      elif cost < b:
        amount = cost if cost > amount else amount
        break
  return amount


'''Second attempt: faster in some condition
The same as above, but in case there is no enough money,
no need to go through all the loop, and exit immediateley 
'''

def getMoneySpent2(keyboards, drives, b):
  keyboards.sort(reverse = True)
  drives.sort(reverse = True)
  if keyboards[-1] + drives[-1] > b:
    return -1
  amount = 0
  for drive in drives:
    for keyboard in keyboards:
      cost = drive + keyboard
      if cost == b:
        return b
      elif cost < b:
        amount = cost if cost > amount else amount
        break
  return amount

