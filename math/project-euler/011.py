# https://projecteuler.net/problem=11
# https://www.hackerrank.com/contests/projecteuler/challenges/euler011/problem


def getVal(ar):
    product = 0
    for i in range(20):
        ar[i] = [1,1,1] + ar[i] + [1,1,1]
    ar += [[1] * 26] * 3
    
    for i in range(20):
        for j in range(3,23):       
            product = max(product,
                ar[i][j] * ar[i+1][j] * ar[i+2][j] * ar[i+3][j],
                ar[i][j] * ar[i][j+1] * ar[i][j+2] * ar[i][j+3],
                ar[i][j] * ar[i+1][j+1]* ar[i+2][j+2] *ar[i+3][j+3],
                ar[i][j] * ar[i+1][j-1] * ar[i+2][j-2] * ar[i+3][j-3]
            )
    return product


if __name__ == '__main__':
    a = [list(map(int,input().split())) for _ in range(20)]
    print(getVal(a))