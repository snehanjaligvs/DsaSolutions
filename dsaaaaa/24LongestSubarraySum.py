def longestSumDivByk(arr, k):
    n = len(arr)
    hashSet = {}
    maxLen  = 0
    currentSum = 0
    for i in range(n):
        currentSum += arr[i]
        mod = ((currentSum%k) + k) % k

        if mod == 0:
            maxLen += 1

        elif mod in hashSet.keys():
            if maxLen < (i - hashSet[mod]):
                maxLen = (i - hashSet[mod])

        else :
            hashSet[mod] = i
    
    return maxLen

arr = [2, 7, 6, 1, 4, 5]
k = 3
print(longestSumDivByk(arr, k))