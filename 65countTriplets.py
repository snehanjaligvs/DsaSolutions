def countTriplets(arr, sum):
    n =len(arr)
    arr.sort()
    count = 0
    for i in range(0, n - 2):
        j = i+1
        k = n-1
        while j < k:
            if arr[i] + arr[j] + arr[k] >= sum :
                k -= 1
            else:
                count += k - j
                j += 1
    return count

arr = [5, 1, 3, 4, 7]
sum = 12
print(countTriplets(arr, sum))