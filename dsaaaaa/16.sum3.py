def threeSum(arr):
    n = len(arr)
    flag = False
    arr.sort()
    for i in range(0, n - 2):
        b = i + 1
        c = n - 1
        while b < c:
            if arr[i] + arr[b] + arr[c] == 0:
              print("Triplet is", arr[i], ', ', arr[b], ', ', arr[c])
              b += 1
              c -= 1
              flag = True
        
            elif arr[i] + arr[b] +arr[c] > 0:
             c -= 1
            else :
             b += 1
            
    if (flag == False):
        print(" No Triplet Found")


nums = [0, -1, 2, -3, 1]
print(threeSum(nums))


        
        