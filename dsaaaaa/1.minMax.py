def minMax(arr, low, high):
    arr_max = arr[low]
    arr_min = arr[low]

    if low == high:
        arr_max = arr_min = arr[low]
        return (arr_max, arr_min)

    elif high == low + 1:
        arr_max = max(arr[low], arr[high])
        arr_min = min(arr[low], arr[high])
        return (arr_max, arr_min)

    else:
        mid = (low + high)//2
        max1, min1 = minMax(arr, low, mid)
        max2, min2 = minMax(arr, mid + 1, high)
        return (max(max1, max2), min(min1, min2))

arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = minMax(arr, low, high)
print("maximum and minimum eements respectively are :", arr_max, arr_min)

//time : O(n)
//space: O(logn)