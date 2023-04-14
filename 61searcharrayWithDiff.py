def search(a, x, k):
    n = len(a)
    i = 0
    while i < n:
        if a[i] == x:
            return i
        i = i + max(1, abs(a[i] - x)//k)
    return -1

arr = [2, 4, 5, 7, 7, 6]
x = 6
k = 2
print(search(arr, x, k))