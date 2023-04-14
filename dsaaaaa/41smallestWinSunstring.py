def smallestWin(s, p):
    n = len(p)
    m = len(s)
    if m < n:
        return -1
    
    hashSet = [0] * 256

    result = m + 1
    count = 0

    for i in p:
        hashSet[ord(i)] += 1
        if hashSet[ord(i)] == 1:
            count += 1
    start = 0
    i = 0
    j = 0
    while j < m:
        hashSet[ord(s[j])] -= 1
        if hashSet[ord(s[j])] == 0:
            count -= 1

            while count == 0:
              if result > j - i + 1:
                result = j - i + 1
                start = i

              hashSet[ord(s[i])] += 1
              if hashSet[ord(s[i])] > 0:
                count += 1
              i += 1
        j += 1
    
    return s[start:start+result]

s = "this is a test string"
p = "tist"
print(smallestWin(s, p))


