# https://www.hackerrank.com/challenges/manasa-and-stones/problem

'''
honestly I struggled with this to understand it first, and then to not have time out
Usually with others I found I provided a competitive answers, but this was an exception.
I read the discussion to find a solution and then it was not as good as others
'''

def stones(n, a, b):
    diffs = sorted([a,b])
    min = diffs[0] * (n - 1)
    max = diffs[1] * (n - 1)
    if min == max:
        return str(min)
    a = [str(i) for i in range(min, max + 1, diffs[1] - diffs[0])]
    if a[-1] != str(max):
        a.append(str(max))
    return ' '.join(a)

'''
another good solution I found
'''

def stones1(n, a, b):
  s = set()
  for i in range(n):
    s.add(b*i + (n-i-1) * a)
  return ' '.join(map(str, sorted(s)))

if __name__ == '__main__':
   t = int(input())
   cases = [ [ int(input()) for _ in range(3) ] for _ in range(t)]
   for i in cases:
       print(stones(*i))
  
