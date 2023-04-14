def findMin(arr, low, high):

    if high < low:
        return -1
    if high == low:
        return low
 
    mid = int((low + high)/2)
 
    if mid < high and arr[mid] > arr[mid + 1]:
        return arr[mid + 1]
    if mid > low and arr[mid] < arr[mid - 1]:
        return arr[mid]
    if arr[high] <= arr[mid]:
        return findMin(arr, mid + 1, high)
    return findMin(arr, low, mid - 1)

arr1 = [5, 6, 1, 2, 3, 4]
n = len(arr1)
print(findMin(arr1, 0, n - 1))