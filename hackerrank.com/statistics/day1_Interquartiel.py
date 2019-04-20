def createDuplicate(data, freq):
  return [y for x in zip(data, freq) for y in [x[0]] * x[1]]

def median(arr):
  count = len(arr)
  if count % 2 == 0:
    return (arr[count // 2] + arr[(count // 2) - 1]) / 2
  else:
    return arr[count // 2]

if __name__ == '__main__':
    count = int(input().rstrip())
    data = list(map(int, input().rstrip().split()))
    freq = list(map(int, input().strip().split()))
    numbers = sorted(createDuplicate(data, freq))
    count = len(numbers)
    if count % 2 == 0:
      lower = numbers[:(count // 2)]
      upper = numbers[count // 2:]
    else:
      lower = numbers[: count // 2]
      upper = numbers[count // 2 + 1:]

    print('{:.1f}'.format(median(upper) - median(lower)))
