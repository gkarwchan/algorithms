def naive_pattern_search(pattern, text):
  founds = []
  currentMatches = [0]
  for i in range(len(text)):
    if text[i] == pattern[currentPatternIndex]:
      currentPatternIndex += 1
      if currentPatternIndex == len(pattern):
        founds.append(i - len(pattern) + 1)
        currentPatternIndex = 0
    else:
      currentPatternIndex = 0
  return founds



if __name__ == '__main__':
  txt = 'AABAACAADAABAABA' #input()
  pattern = 'AABA' # input()
  result = naive_pattern_search(pattern, txt)
  print (result)
