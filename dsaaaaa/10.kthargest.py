def kthLargest(arr, k):
    arr.sort()
    return arr[len(arr) - k]

arr = [3,2,1,5,6,4]
k = 2
print(kthLargest(arr, k))