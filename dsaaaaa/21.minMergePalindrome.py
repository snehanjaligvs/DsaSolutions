def minMerge(arr):
    res = 0
    i = 0
    j = len(arr) - 1
    while i <= j :
        if arr[i] == arr[j]:
            j -= 1
            i += 1
        
        elif arr[i] > arr[j]:
            arr[j-1] += arr[j]
            j -= 1
            res += 1
        else:
            arr[i + 1] += arr[i]
            i += 1
            res += 1
    return res

arr = [1, 4, 5, 9, 1]
print(minMerge(arr))