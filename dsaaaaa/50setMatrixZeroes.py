def setZero(arr):
    row = len(arr)
    col = len(arr[0])
    Col = False
    Row = False
    for i in range(row):
        if (arr[i][0] == 0)  :
          Col = True
    for j in range(col):
        if arr[0][j] == 0:
            Row = True
    for i in range(1, row):  
        for j in range(1, col):
            if arr[i][j] == 0:
                arr[i][0] = 0
                arr[0][j] = 0

    for i in range(1, row):
        for j in range(1, col):
            if arr[0][j] == 0 or arr[i][0] == 0:
                arr[i][j] = 0

    if Row == True:
        for j in range(col):
            arr[0][j] = 0
            
    if Col == True:
        for i in range(row):
            arr[i][0] = 0

matrix = [[1,1,0],[1,0,1],[1,1,1]]
setZero(matrix)
print(matrix)