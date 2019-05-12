
# https://www.hackerrank.com/challenges/fair-rations/problem

def fairRations(B):
    breads = 0
    for i in range(len(B) - 1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i+1] += 1
            breads += 2
    return str(breads) if B[-1] % 2 == 0 else 'NO'
        
    


if __name__ == '__main__':
    n = int(input())
    B = list(map(int, input().split()))

    print (fairRations(B))