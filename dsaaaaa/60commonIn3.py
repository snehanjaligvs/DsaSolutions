def common(a1, a2, a3):
    n1 = len(a1)
    n2 = len(a2)
    n3 = len(a3)
    i, k,j = 0, 0, 0
    while i < n1 and j < n2 and k < n3:
        if a1[i] == a2[j] and a2[j]== a3[k]:
            print(a1[i])
            i += 1
            j += 1
            k += 1
        elif a1[i] < a2[j]:
            i += 1
        elif a2[j]  < a3[k]:
            j += 1
        else:
            k += 1

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
common(ar1, ar2, ar3)
