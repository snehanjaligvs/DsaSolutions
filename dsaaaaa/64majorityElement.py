def majority(arr):
    n = len(arr)
    hashSet = {}
    for i in arr:
        if i not in hashSet:
            hashSet[i] = 1
        hashSet[i] += 1
    flag = 0
    for key in hashSet:
        if hashSet[key] > (n//2 + 1):
            flag = 1
            print("majority element : " , key)
            break
    if not flag:
        print("No majority element")

arr = [1, 3, 3, 1, 2]
majority(arr)