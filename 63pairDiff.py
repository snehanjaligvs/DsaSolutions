def pairDiff(arr, n):
    hashSet = {}
    l = len(arr)
    for i in arr:
        if i not in hashSet:
            hashSet[i] = 1
        else:
            hashSet[i] += 1
            if n == 0 and hashSet[i] > 1:
                print("pair is : (", i, " ,", i, ")")
                return True
    if n == 0:
        return False
    for i in range(l):
        if n + arr[i] in hashSet.keys():
            print("pair is : (", arr[i], " ,", n + arr[i], ")")
            return True
    print("pair not found")
    return False

arr = [5, 20, 3, 2, 50, 80]
n = 78
pairDiff(arr, n)