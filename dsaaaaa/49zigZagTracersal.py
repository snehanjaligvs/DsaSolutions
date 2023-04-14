def zigZag(arr):
     row = 5
     col = 4
     for k in range(0, row):
        print(arr[k][0], end = " ")

        i = k - 1
        j = 1

        while (not(i < 0 or i >= row or j >= col or j < 0)):
            print(arr[i][j], end = " ")
            i -=1
            j += 1
        
        print()

     for k in range(1, col):
        print(arr[row-1][k], end = " ")

        i = row - 2
        j = k + 1
        while (not(i < 0 or i >= row or j >= col or j < 0)):
            print(arr[i][j], end = " ")
            i -= 1
            j += 1
        print()

arr = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16],
       [17, 18, 19, 20]]
zigZag(arr)