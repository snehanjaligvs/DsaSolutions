def longestPalinSubstring(s):
        n = len(s)
        maxlen = 1
        table = [[0 for i in range(n)] for j in range(n)]

        l = 0
        while l < n:
            table[l][l] = True
            l += 1

        start = 0
        l = 0
        while l < n-1:
            if s[l] == s[l + 1]:
                table[l][l+1] = True
                start = l
                maxlen = 2
            l += 1
        
        k = 3
        while k <= n:
            l = 0
            while l < (n - k + 1):
                j = l + k - 1
                if table[l + 1][j - 1] == True and s[l] == s[j]:
                    table[l][j] = True

                    if  k > maxlen:
                        start = l
                        maxlen = k
                l += 1
            k += 1

        str =""
        for i in range(start, start + maxlen):
            str += s[i]
        return str
            
s = 'babad'
print(longestPalinSubstring(s))