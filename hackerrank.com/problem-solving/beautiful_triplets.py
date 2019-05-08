# Web location
# https://www.hackerrank.com/challenges/beautiful-triplets/problem

if __name__ == '__main__':
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    dictd = {}
    for i in arr:
          if i in dictd:
                dictd[i][0] += 1
          else:
                dictd[i] = [1,0,0]
          if i - d >= 0 and i - d in dictd:
                dictd[i-d][1] += 1
          if i - 2 * d >= 0 and i - 2 * d in dictd:
                dictd[i-2*d][2] += 1
    
    result = sum([dictd[k][0] * dictd[k][1] * dictd[k][2] for k in dictd])
    print (result)



