from itertools import zip_longest

def sumLists(list1, list2):
  result = []
  curry = 0
  for i, j in zip_longest(list1, list2, fillvalue=0):
    print(i, j)
    sum = i + j + curry
    if sum > 10:
      result.append(sum % 10)
      curry = int(sum / 10)
    else:
      curry = 0
      result.append(sum)
  if curry:
    result.append(curry)
  return result



if __name__ == '__main__':
  list1 = [9, 9]
  list2 = [5, 2]
  print(sumLists(list1, list2))
