class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)

        if len_s == 0:
            return True
        if len_t == 0:
            return False

        i_s = 0
        i_t = 0
        while i_t < len_t and i_s<len_s:
            if s[i_s] == t[i_t]:
                i_s+=1
                i_t+=1
                continue
            i_t+=1

        if i_s==len_s:
            return True
        else:
            return False


# I don't think it is a DP problem
# The idea is checking s[index_s] with t[index_t], if match, both +1, else index_t +1
