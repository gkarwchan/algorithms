# https://www.hackerrank.com/challenges/sock-merchant/problem

from collections import Counter

def sockMerchant(n, ar):
    c = Counter(ar)
    return sum([c[i] // 2 for i in c])
    
    
    
        
if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().split()))
    print(sockMerchant(n, ar))

    