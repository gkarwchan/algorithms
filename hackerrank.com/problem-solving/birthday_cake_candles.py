# https://www.hackerrank.com/challenges/birthday-cake-candles/problem


def birthdayCakeCandles(arr):
    return arr.count(max(arr))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(birthdayCakeCandles(arr))
    
