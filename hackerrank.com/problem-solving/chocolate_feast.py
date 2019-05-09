# Web location
# https://www.hackerrank.com/challenges/chocolate-feast/problem

def chocolateFeast(total, bar, wrap, m):
      total += bar
      if (bar + wrap) // m == 0:
            return total
      return chocolateFeast(total, (bar + wrap) // m, (bar + wrap) % m, m)



if __name__ == '__main__':
      n = int(input())
      inputs = [list(map(int, input().split())) for _ in range(n)]
      outputs = [str(chocolateFeast(0, i[0] // i[1], 0, i[2])) for i in inputs]
      print ('\n'.join(outputs))

