def longestSumDivByk(str):
    n = len(str)
    if n == 0:
        return 0
    hash = set()
    hash.add(str[0])
    maxLen  = 0
    currentLen = 1
    i = 1
    while i < n:
        
        if str[i] != str[i - 1] and str[i] not in hash:
            currentLen += 1
            hash.add(str[i])
            i += 1
            if maxLen < currentLen:
                maxLen = currentLen
        else:
            if currentLen == 1:
                i += 1
            else:
                hash.clear()
                i = i - currentLen + 1
                currentLen = 0
        
    return max(maxLen, currentLen)

s = "abcabcbb"
print(longestSumDivByk(s))