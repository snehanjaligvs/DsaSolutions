def countSort(arr):
    ans = [0]* len(arr)
    b = max(arr)
    a = min(arr)
    k = b - a+1
    count = [0]*(k)
    for i in range(len(arr)):
        count[arr[i]-a] += 1
    for i in range(1, len(count)):
        count[i] = count[i-1] + count[i]
    for i in range(len(arr) - 1, -1, -1):
        ans[count[arr[i]-a] - 1] = arr[i]
        count[arr[i] - a] -= 1
    return ans

arr = [-5, -10, 0, -3, 8, 5, -1, 10]
print(countSort(arr))