'''
assuming the list is not sorted, because the problem text didn't specify that
'''

def findContiguous(list, k):
  solutions = []
  for i in range(len(list)):
    sum = list[i]
    while sum < k and :
      j = i + 1
      sum += list[i+1]
    if sum == k:
      solutions.append()
  return list
  

if __name__ == '__main__':
  input = [1,2,3,4,5]
  print(findContiguous(input, 9))