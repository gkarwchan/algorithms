# https://www.hackerrank.com/challenges/cavity-map/problem

def cavityMap(grid):
   for i in range(1, len(grid) - 1):
       for j in range(1, len(grid) - 1):
           if grid[j][i- 1] < grid[j][i] > grid[j][i + 1] and grid[j-1][i] < grid[j][i] > grid[j+1][i]:
               grid[j][i] = 'X'
   return '\n'.join([''.join(i) for i in grid])


if __name__ == '__main__':
   n = int(input())
   grid = [list(input()) for _ in range(n)]
   print(cavityMap(grid))
  
