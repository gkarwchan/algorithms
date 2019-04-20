def createDuplicate(values, frequencies):
  

def median(arr):
  count = len(arr)
  if count % 2 == 0:
    return (arr[count // 2] + arr[(count // 2) - 1]) / 2
  else:
    return arr[count // 2]

if __name__ == '__main__':
    count = int(input().rstrip())
    numbers = sorted(list(map(int, input().rstrip().split())))
    if count % 2 == 0:
      lower = numbers[:(count // 2)]
      upper = numbers[count // 2:]
    else:
      lower = numbers[: count // 2]
      upper = numbers[count // 2 + 1:]
    print (int(median(lower)))
    print (int(median(numbers)))
    print (int(median(upper)))

