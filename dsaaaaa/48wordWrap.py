def wordWrap(arr, k):
    n = len(arr)
    i = 0
    j = 0
    cost = 0
    while j < n - 1:
        if arr[j] + arr[j + 1] + 1 <= k:
            cost += (k - arr[j] - arr[j + 1] - 1)**2
            i += 1
            if arr[i] + arr[i + 1] + 1 <= k:
                cost = 0 
                cost += (k - arr[j])**2 + (k - arr[i] - arr[i + 1] - 1)**2
                j = i +  1
        else :
            cost += (k - arr[j])**2

        j += 1
    return cost

arr = [3, 2, 2, 5]
k = 6
print(wordWrap(arr, k))

#cost += (k - arr[j] - arr[j + 1] - 1)**2
            #i += 1
            #if arr[i] + arr[i + 1] + 1 <= k:
                #cost = 0 
                #cost += (k - arr[j])**2 + (k - arr[i] - arr[i + 1] - 1)**2
                #j = i + 1