def search(arr, low, high, target):
    if low > high :
        return -1
    mid = (low + high)//2
    if arr[mid] == target:
        return mid
    
    if arr[low] <= arr[mid]:
        if target >= arr[low] and target <= arr[mid]:
            return search(arr,low, mid - 1, target)
        return search(arr, mid + 1, high, target)
    if target >= arr[mid] and target <= arr[high]:
        return search(arr,mid + 1,high, target )
    return search(arr, low, mid - 1, target)

arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 9
print(search(arr, 0, len(arr) - 1, key))