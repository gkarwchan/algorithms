# https://projecteuler.net/problem=6
# https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem

def sumsquarediff(n):
    sum_square = (2 * n**3 + 3 * n ** 2 + n) // 6
    square_sum = ((n * (n+1)) // 2) ** 2
    return square_sum - sum_square


if __name__ == '__main__':
    for _ in range(int(input())):
        print (sumsquarediff(int(input())))