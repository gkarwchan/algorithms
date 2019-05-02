
def cutTheSticks(sticks):
    uniques = sorted(set(sticks))
    total = len(sticks)
    result = []
    lengths = {i: sticks.count(i) for i in uniques}
    for j in lengths:
        result.append(total)
        total -= lengths[j]
    return result    


if __name__ == '__main__':
    n = int(input())
    sticks = list(map(int, input().split()))
    result = cutTheSticks(sticks)
    print (result)

        

        


