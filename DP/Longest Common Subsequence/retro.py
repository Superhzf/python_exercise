def longestCommonSubsequence(text1, text2):
    if len(text1) == 0 or len(text2) == 0:
        return 0

    dp = [[0 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]

    for this_text1 in (1,len(text1)+1):
        for this_text2 in (1, len(text2)+1):
            if text1[this_text1-1] == text2[this_text2-1]:
                dp[this_text1][this_text2] = dp[this_text1-1][this_text2-1]+1
            else:
                dp[this_text1][this_text2] = max(dp[this_text1-1][this_text2],
                                                 dp[this_text1][this_text2-1])
    return dp[-1][-1]
