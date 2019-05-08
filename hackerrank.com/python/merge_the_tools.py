# https://www.hackerrank.com/challenges/merge-the-tools/problem

'''
first simple attempt
'''

def merge_the_tools(string, k):
    u = [string[i*k:i*k+k] for i in range(len(string) // k)]
    for s in u:
        o = dict([(i, 0) for i in s])
        print (''.join(o.keys()))


'''
second smarter attempt
'''

def merge_the_tools1(string, k):
    for i in range(0,len(string), k):
        d = dict([(c, 0) for c in string[i:i+k]])
        print (''.join(d.keys()))


if __name__ == '__main__':
    s = input()
    k = int(input())
    merge_the_tools(s, k)