# https://projecteuler.net/problem=5
# https://www.hackerrank.com/contests/projecteuler/challenges/euler005/problem

def gcd(a, b):
    while(b):
        a, b = b, a%b
    return a

def lcm(a, b=None, *rest):
    if b == None:
        return a
    rslt = (a*b) // gcd(a, b)
    if rest:
        return lcm(rslt, rest[0], *rest[1:])
    else:
        return rslt
        
    


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        numbers = [x for x in range(1, n + 1)]
        print (lcm(*numbers))