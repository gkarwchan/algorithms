'''
weighted mean
'''

if __name__ == '__main__':
  count = int(input().rstrip())
  numbers = list(map(int, input().rstrip().split()))
  weights = list(map(int, input().rstrip().split()))
  
  weightedValues = list(map(lambda num, w: num * w, numbers, weights))
  weightedMean = round(sum(weightedValues) / sum(weights), 1)
  print(weightedMean)
