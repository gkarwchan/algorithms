# https://www.hackerrank.com/challenges/diagonal-difference/problem


def diagonalDifference(arr):
    axs = [(arr[i][i], arr[i][len(arr) - 1 - i]) for i in range(len(arr))]
    return abs(sum ([i[0] for i in axs]) - sum ([i[1] for i in axs]))

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    print(diagonalDifference(arr))