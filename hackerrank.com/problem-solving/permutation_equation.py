'''
Straight implementation
Pros: easy to understand and match the problem description
Cons: Slow
'''
def permutationEquation(p):
    return [p.index(p.index(i)+1) + 1 for i in range(1, len(p) + 1)]


'''
reverse implementation
Pros: fast
Cons: need a bit of thinking to understand
'''

def permutationEquation2(p):
    dct = { val: i + 1 for i, val in enumerate(p)}
    return [dct[dct[j]] for j in range(1, len(p) + 1)]




if __name__ == '__main__':
    n = int(input())
    p = list(map(int, input().rstrip().split()))
    result = permutationEquation(p)
    print('\n'.join(map(str, result)))

