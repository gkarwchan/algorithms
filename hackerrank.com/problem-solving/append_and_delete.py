# web location
# https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s1, s2, k):
    common = 0
    while common < len(s1) and common < len(s2) and s1[common] == s2[common]:
        common += 1
    moves = len(s1) + len(s2) - 2 * common
    if k >= moves and (k - moves) % 2 == 0:
        return 'Yes'
    if k >= moves + common * 2:
        return 'Yes'
    else:
        return 'No'
    



if __name__ == '__main__':
    result = appendAndDelete(input().rstrip(), input().rstrip(), int(input().rstrip()))
    print (result+ '\n')
        

        


