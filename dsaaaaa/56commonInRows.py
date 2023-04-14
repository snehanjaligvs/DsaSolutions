from collections import defaultdict
def findCommon(mat):
    m = len(mat)
    n = len(mat[0])
    hashSet = dict()
    hashSet = defaultdict(lambda: 0, hashSet)
    i = 0
    j = 0
    while i < m:
        hashSet[mat[i][0]] = hashSet[mat[i][0]] + 1
        j = 1
        while j < n:
            if mat[i][j] != mat[i][j - 1]:
                hashSet[mat[i][j]] += 1
            j += 1
        i += 1
    for i in hashSet:
        if hashSet[i] == m:
            return i
    return -1


mat = [[1, 2, 3, 4, 5 ],
        [2, 4, 5, 8, 10],
        [3, 5, 7, 9, 11],
        [1, 3, 5, 7, 9 ],]
print(findCommon(mat))