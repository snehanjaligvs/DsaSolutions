def permuOfR(arr, n, r):
    data = [0]*r

    CombUntil(arr, n, r ,0, data, 0)

    def CombUntil(arr, n, r, ind, data, i):
        if index == r:
            for j in range(r):
                print(data[j])
            return
        
        data[ind] = arr[i]
        CombUntil(arr, n, r, ind + 1, data, i)

        ComdUntil(arr, n, r, ind, data, i +1)



arr = [1, 2, 3, 4, 5]
r = 3
n = len(arr)
print(permuOfR(arr,n, r ))