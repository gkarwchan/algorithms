def naive_pattern_search(pattern, text):
  founds = []
  patternIndices = []
  for i in range(len(text)):
    j = 0
    while j < len(patternIndices):
      if text[i] == pattern[patternIndices[j]]:
        patternIndices[j] += 1
        if patternIndices[j] == len(pattern):
          founds.append(i - len(pattern) + 1)
          del patternIndices[j]
        else:
          j += 1
      else:
        del patternIndices[j]
    if text[i] == pattern[0]:
      if len(pattern) == 1:
        founds.append(i)
      else:
        patternIndices.append(1)
    
      
  return founds



if __name__ == '__main__':
  txt = 'AABAACAADAABAABA' #input()
  pattern = 'AABA' # input()
  result = naive_pattern_search(pattern, txt)
  print (result)
