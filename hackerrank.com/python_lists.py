'''
using eval
'''

if __name__ == '__main__':
    l = []
    c = [input() for _ in range(int(input()))]
    for line in c:
      if line == 'print':
        print(l)
      else:
        words = line.split(' ')
        cmd = "l.{}({})".format(words[0], ','.join(words[1:]))
        eval(cmd)

'''
another attempt using function's getattr
''''
if __name__ == '__main__':
    l = []
    c = [input() for _ in range(int(input()))]
    for line in c:
      if line == 'print':
        print(l)
      else:
        words = line.split(' ')
        getattr(l, words[0])(*list(map(int, words[1:])))
