def longestCommonPrefix(strs):
        result = ""
        if len(strs) == 1:
            return strs[0]
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(len(strs)):
                if (i == len(strs[j]) or strs[j][i] != c):
                    return result
            result += strs[0][i]

        return result

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))