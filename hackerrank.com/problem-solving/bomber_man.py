# https://www.hackerrank.com/challenges/bomber-man/problem

def leftShift(x): return x & ( (x << 1) | 1)
def rightShift(x, topValue): return x & ( (x >> 1) | topValue)
def oneComplement(x, length): return ((1 << length) - 1) ^ x
def convertToString(grid, rowWidth):
    formatString = '0{0}b'.format(rowWidth)
    a = [format(x, formatString).replace('0', '.').replace('1', 'O') for x in grid]
    return '\n'.join(a)

def ind(index, topValue): return 0 if index == -1 else topValue -1 if index == topValue else index
    

def bomberMan(n, grid):
    rowWidth = len(grid[0])
    rows = len(grid)
    oneLeft = int('1' + '0' * (rowWidth - 1), 2)

    if (n == 0 or n == 1): return '\n'.join(grid)
    if n % 2 == 0: return '\n'.join(['O' * rowWidth ] * rows)
    t = [int(x.replace('.', '1').replace('O', '0'), 2) for x in grid]
    thirdSecond = [x & t[ind(i-1, rows)] & t[ind(i + 1, rows)] & leftShift(x) & rightShift(x, oneLeft) for i, x in enumerate(t)]
    if (n + 1) % 4 == 0: return convertToString(thirdSecond, rowWidth)
    t = [oneComplement(x, rowWidth) for x in thirdSecond]
    fifthSecond = [x & t[ind(i-1, rows)] & t[ind(i + 1, rows)] & leftShift(x) & rightShift(x, oneLeft) for i, x in enumerate(t)]
    return convertToString(fifthSecond, rowWidth)

if __name__ == '__main__':
    r, c, n = map(int, input().split())
    ar = [input() for _ in range(r)]
    result = bomberMan(n, ar)
    print(result)

