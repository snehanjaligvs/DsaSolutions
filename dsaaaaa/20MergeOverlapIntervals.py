def mergeInterval(arr):
    arr.sort()
    index = 0
    for i in range(1, len(arr)):
        if arr[index][1] >= arr[i][0]:
            arr[index][1] = max(arr[index][1], arr[i][1])
        else :
            index = index + 1
            arr[index] = arr[i]

    print("Merged intervals :")
    for i in range(0, index + 1):
        print(arr[i])

arr = [[1, 3], [2, 4], [4, 7], [8, 9]]
mergeInterval(arr)
