# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

'''
without importing ascii
'''


def print_rangoli(size):
    chars = [chr(i + ord('a')) for i in range (size -1, -1, -1)]
    output = ['-'.join(chars[:i] + chars[i::-1]).center(4 * size - 3, '-') for i in range(size)]
    print ('\n'.join(output + output[-2::-1]))




'''
with importing ascii
'''
import string

def print_rangoli2(size):
    chars = string.ascii_lowercase
    output = ['-'.join(chars[:i] + chars[i::-1]).center(4 * size - 3, '-') for i in range(size)]
    print ('\n'.join(output + output[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
