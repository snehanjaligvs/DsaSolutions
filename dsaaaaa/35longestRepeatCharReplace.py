def longestRepeatCharReplace(s, k):
        i = 0
        hashSet = {}
        maxLen = 0
        maxFreq = 0
        for j in range(len(s)):
            hashSet[s[j]] = 1 + hashSet.get(s[j], 0)
            maxFreq = max(maxFreq, hashSet[s[j]])
            
            while (j - i + 1) - maxFreq > k :
                hashSet[s[i]] -= 1
                i += 1

            maxLen = max(maxLen, j - i + 1)
            
        return maxLen

s = "ABAB"
k = 2
print(longestRepeatCharReplace(s, k))