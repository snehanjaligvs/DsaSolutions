def prodArrayExcept(nums):
        n = len(nums)
        before = [0] * n
        after = [0] * n
        product = [1] * n
        before[0] = 1
        after[n-1] = 1
        for i in range(1, n):
            before[i] = nums[i - 1] * before[i - 1]

        for i in range(n-2, -1, -1):
            after[i] = nums[i + 1] * after[i + 1]
        
        for i in range(n):
            product[i] = before[i] * after[i]

        return product

arr = [1, 2, 3, 4]
print(prodArrayExcept(arr))