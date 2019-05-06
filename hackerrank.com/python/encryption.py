# web location
# https://www.hackerrank.com/challenges/encryption/problem

import math

def encryption(s):
    msg = s.replace(' ', '')
    columns = math.ceil(math.sqrt(len(msg)))
    ar = [msg[i:i+columns] for i in range(0, len(msg), columns)]
    ar[-1] = ar[-1].ljust(columns)

    return ' '.join([''.join(list(j)).replace(' ', '') for j in zip(*ar)])



if __name__ == '__main__':
    s = input()
    print(encryption(s))

