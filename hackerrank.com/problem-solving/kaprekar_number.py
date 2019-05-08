# Web location
# https://www.hackerrank.com/challenges/kaprekar-numbers/problem

if __name__ == '__main__':
    p = int(input())
    q = int(input())
    result = []
    for i in range(p, q+1):
        s = str(i*i).rjust(2, '0')
        n1, n2 = int(s[0:len(s) // 2]), int(s[len(s)//2:])
        if n1 + n2 == i:
            result.append(str(i))
    print (' '.join(result) if len(result) > 0 else 'INVALID RANGE')