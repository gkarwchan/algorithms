if __name__ == '__main__':
  count = int(input().rstrip())
  numbers = sorted(list(map(int, input().rstrip().split())))
  
  mean = round(sum(numbers) / count, 2)
  middle = count // 2
  if count % 2 == 0:
    median = (numbers[middle] + numbers[middle - 1]) / 2
  else:
    median = numbers[int(middle)]

  counter = { i : 0 for i in numbers}
  for number in numbers:
    counter[number] += 1
  sortVal = [k for k in sorted(counter, key=counter.get, reverse=True)]
  mode = sortVal[0]

  print(mean)
  print(median)
  print (mode)