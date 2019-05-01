def jumpingOnClouds(c, k):
    energyConsumption = sum([c[i % len(c)] * 2 for i in range(0, len(c) + 1, k)]) + len(c) // k
    lastStep = 0 if len(c) % k == 0 else c[0] * 2 + 1
    return 100 - energyConsumption - lastStep

if __name__ == '__main__':
    p,k = list(map(int, input().rstrip().split()))
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c, k)
    print(result)


        

        


