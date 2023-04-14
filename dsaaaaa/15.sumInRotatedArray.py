def findPivot(arr, low, high):
 
    if high < low:
        return -1
    if high == low:
        return low
 
    mid = int((low + high)/2)
 
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return (mid-1)
    if arr[low] >= arr[mid]:
        return findPivot(arr, low, mid-1)
    return findPivot(arr, mid + 1, high)

def findSum(arr, low, high , target):
    n = len(arr)
    i = findPivot(arr, low, high)
    high = i
    low = (i + 1)%n
    while low != high:
        if arr[low] + arr[high] == target:
          return True
        if arr[low] + arr[high] <target :
          low = (low + 1)%n
        else  :
          high = (n + high - 1)%n

    return False


arr = [11, 15, 26, 38, 9, 10]
n = len(arr)
target = 35
if (findSum(arr, 0, n - 1, target)):
    print("true")
else :
    print("false")