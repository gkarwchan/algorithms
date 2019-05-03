if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    counts = {i : arr.count(i) for i in set(arr)}
    sortCount = sorted(counts, key = counts.get, reverse=True)
    print (len(arr) - arr.count(sortCount[0]))
    
    