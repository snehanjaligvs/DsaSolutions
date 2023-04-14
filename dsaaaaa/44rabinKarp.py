def rabinKarp(text, pat):
    q = 11
    n = len(text)
    m = len(pat)
    i = 0
    j = 0
    p =0 
    t = 0
    h = 1
    d = 256
     
    for i  in range(m - 1):
        h = (h*d) % q

    for i in range(m):
        p = (d*p + ord(pat[i]))%q
        t = (d*t + ord(text[i]))%q

    for i in range(n-m + 1):
        if p == t:
            while j < m:
                if text[i + j] != pat[j]:
                    break
                else :
                        j += 1
                
            if j == m:
                print("pattern found at index :", i)

        if i < n- m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

            if t<0:
                t = t+q
        
text = "AABAACAADAABAABA"
pat = "AABA"
rabinKarp(text, pat)

