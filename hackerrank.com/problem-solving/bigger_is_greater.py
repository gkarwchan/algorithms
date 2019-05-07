# web location
# https://www.hackerrank.com/challenges/bigger-is-greater/problem


def bigerIsGreater(s):
    st = list(s)
    ind = -2
    while ind >= -1 * len(st):
        if st[ind] < st[ind + 1]:
            break
        ind -= 1
    else:
        return 'no answer'
    char = st[ind]
    part1 = st[0:len(st) + ind]
    part2 = sorted(st[len(st) + ind:])
    part2.insert(0, part2.pop(part2.index(char) + part2.count(char)))
    return (''.join(part1 + part2))


if __name__ == '__main__':
    n = int(input())
    outputs = [bigerIsGreater(input()) for _ in range(n)]

    print('\n'.join(outputs))