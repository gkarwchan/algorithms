'''
simple form
'''

def print_formatted(number):
    max_width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=max_width))

'''
to illustrate more, I explicitly added the align with is default to right when width is assigned
'''

def print_formatted1(number):
    max_width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print('{0:{align}{width}d} {0:{align}{width}o} {0:{align}{width}X} {0:{align}{width}b}'.format(i, align='>', width=max_width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# --------------------------------------------------------------

'''
Another way to find the length of the binary
bin(17) = '0b10001'
'''

max_width = len(bin(17)[2:])



