def palindromicStrings(s):
        n = len(s)
        
        table = [[0 for i in range(n)] for j in range(n)]

        l = 0
        while l < n:
            table[l][l] = 1
            l += 1

        l = 0
        while l < n-1:
            if s[l] == s[l + 1]:
                table[l][l+1] = 1
            l += 1
        
        k = 3
        while k <= n:
            l = 0
            while l < (n - k + 1):
                j = l + k - 1
                if table[l + 1][j - 1] == 1 and s[l] == s[j]:
                    table[l][j] = 1
                l += 1
            k += 1

        count = 0
        for i in range(n):
            for j in range(n):
                if table[i][j] == 1:
                    count += 1
        return count

s = "aaa"
print(palindromicStrings(s))