def isSubsequence(s, t):
    if len(t) == 0:
        return False
    if len(len(s)) == 0:
        return True

    i_s = 0
    i_t = 0
    while i_s < len(s) and i_t<len(t):
        if s[i_is] == t[i_t]:
            i_s += 1
            i_t += 1
            continue
        i_t += 1
    if i_s == len(s):
        return True
    else:
        return False
