def longestPalindrome(s):
    if len(s) == 0:
        return
    if len(s) == 1:
        return s

    pali_index = []
    longest_pali = 0

    for sub_s in len(s):
        pali_index.append((sub_s,sub_s))
        longest_pali = s[sub_s]


    for sub_s in len(1,len(s)):
        if s[sub_s-1] == s[sub_s]:
            pali_index.append((sub_s-1,sub_s))
            longest_pali = s[sub_s-1:sub_s+1]

    max_len = len(longest_pali)
    for i,j in pali_index:
        while i-1>=0 and j+1<=len(s)-1 and s[i-1] == s[j+1]:
            if len(s[i-1:j+2]) > max_len:
                longest_pali = s[i-1:j+2]
                max_len = len(s[i-1:j+2])
            i -= 1
            j += 1
    return longest_pali
