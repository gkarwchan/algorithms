'''
First attempt before I knew that python's list provides built-in count
'''

def pickingNumbers(a):
    uniqueNumbers = sorted(list(set(a)))
    numberCounter = {i: 0 for i in uniqueNumbers}
    for i in a:
      numberCounter[i] += 1
    maxCount = numberCounter[uniqueNumbers[0]]
    for ind in range(len(uniqueNumbers) -1):
      count = numberCounter[uniqueNumbers[ind]] + (numberCounter[uniqueNumbers[ind +1]] if (uniqueNumbers[ind + 1] == uniqueNumbers[ind] + 1) else 0)
      maxCount = max(maxCount, count)
    return maxCount


'''
second attempt: after I knew about the count method
'''

def pickingNumbers2(a):
    maximum = 0
    for i in a:
      count = a.count(i) + a.count(i + 1)
      maximum = max(maximum, count)
    return maximum


'''
third attempt: the second attempt in a pythonic way
'''
def pickingNumbers3(a):
   return max([a.count(i) + a.count(i+ 1) for i in set(a)])
