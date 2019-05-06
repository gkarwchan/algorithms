# Weblocation
# https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

def organizingContainers(container):
    containerSizes = sorted([sum(types) for types in container])
    typeSizes = sorted([sum(i) for i in zip(*container)])
    possible = all(item[0] == item[1] for item in zip(containerSizes, typeSizes))
    return 'Possible' if possible else 'Impossible'


if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        n = int(input())
        container = [list(map(int, input().split())) for _ in range(n)]
        result = organizingContainers(container)
        print(result + '\n')

    