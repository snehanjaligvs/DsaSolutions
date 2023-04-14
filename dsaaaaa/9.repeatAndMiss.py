def swap(arr, a, b):
	temp = arr[a]
	arr[a] = arr[b]
	arr[b] = temp

def repeatAndMissing(arr):
    n = len(arr)
    i = 0
    repeat = missing = 0
    while i < n:
        if arr[i] == arr[arr[i] - 1]:
            i += 1
        else:
            swap(arr, i, arr[i] - 1)

    for i in range(n):
        if arr[i] != i + 1:
            repeat = arr[i]
            missing = i + 1
            break
    print("repeating num :", repeat)
    print("missing num :", missing)

arr = [4, 3, 6, 2, 1, 6, 7]
repeatAndMissing(arr)

        