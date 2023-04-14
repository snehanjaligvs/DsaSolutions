def validAnagram(s, t) :
        noOfChars = 256
        if len(s) != len(t):
            return False
        count1 = [0]*noOfChars
        count2 = [0]*noOfChars
        for i in s:
            count1[ord(i)] += 1
        for i in t:
            count2[ord(i)] += 1
        for j in range(noOfChars):
            if count1[j] != count2[j]:
                return False
        return True

s = "rat"
t = "car"
if validAnagram(s, t):
    print("they are anagrams")
else:
    print("they are not anagrams")
