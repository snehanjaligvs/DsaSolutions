def replaceObyX(mat):
    n = len(mat)
    m = len(mat[0])
    for i in range(1, n-1):
        for j in range(1, m -1):
            if mat[i][j] == 'O':
                if (mat[i][j + 1] == 'X' and mat[i][j - 1] == 'X' and mat[i - 1][j] == 'X' and mat[i+1][j ] == 'X'):
                    mat[i][j] = 'X'

    return mat
mat = [ [ 'X', 'O', 'X', 'O', 'X', 'X' ],
            [ 'X', 'O', 'X', 'X', 'O', 'X' ],
            [ 'X', 'X', 'X', 'O', 'X', 'X' ],
            [ 'O', 'X', 'O', 'X', 'X', 'X' ],
            [ 'X', 'X', 'X', 'O', 'X', 'O' ],
            [ 'O', 'O', 'X', 'O', 'O', 'O' ] ]
 
print(replaceObyX(mat))