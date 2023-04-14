def isPalindrome( s) :
        l = 0
        h = len(s) - 1
        s  = s.lower()
        while l <= h :
            if (not((s[l]>='a' and s[l]<='z') or (s[l]>='0' and s[l]<='9'))):
                l += 1
            elif (not((s[h]>='a' and s[h]<='z') or (s[h]>='0' and s[h]<='9'))) :
                h -= 1
            elif (s[l] == s[h]):
                l += 1
                h -= 1
            else:
                return False

        return True

s = "A man, a plan, a canal: Panama"
if isPalindrome(s):
    print(" it is a palindrome")
else:
    print("not a palindrome")