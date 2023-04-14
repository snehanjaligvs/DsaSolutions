def maxSubArray(arr):
    curmax = arr[0]
    globalmax = arr[0]

    for i in range(1, len(arr)):
        curmax = max(arr[i], arr[i] + curmax)

        if curmax > globalmax :
            globalmax = curmax
            endind = i

    startind = endind

    while startind >= 0:
        globalmax -= arr[startind]
        if globalmax == 0:
            break
        startind -= 1
    
    for i in range(startind, endind + 1):
        print(arr[i])


arr = [ 2, 3, -2, -4, 4]

maxSubArray(arr)