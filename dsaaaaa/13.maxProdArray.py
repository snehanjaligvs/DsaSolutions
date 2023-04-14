def maxProdArray(arr):
    n = len(arr)
    maxTillThen = arr[0]
    minTillThen = arr[0]
    maxTotal = arr[0]
    for i in range(1, n):
        temp = max(arr[i], maxTillThen*arr[i], minTillThen*arr[i])
        minTillThen = min(arr[i], maxTillThen*arr[i], minTillThen*arr[i])
        maxTillThen = temp
        maxTotal = max(maxTillThen, maxTotal)
    return maxTotal

    

arr = [1, -2, -3, 0, 7, -8, -2]
print(maxProdArray(arr))