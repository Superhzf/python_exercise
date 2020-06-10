class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0

        num_decode = [0]*len(s)
        num_decode[0] = 1

        for i in range(1,len(s)):
            if s[i] != '0': # '1'-'9', 将s[:i-1]和s[i]视为两部分
                num_decode[i] += num_decode[i-1]

            if 10<=int(s[i-1:i+1])<=26: # 将s[:i-2]和s[i-1:i+1]视为两部分
                if i == 1: # if it is s[1], s only has two chars
                    num_decode[i] +=1
                    continue
                num_decode[i]+=num_decode[i-2]

        return num_decode[-1]


# enumerate all possible solutions:
# Suppose the input is 1234567, then the solution tree could be like this:
#                       1234
#                   /   |      \
#                1,234 12,34    123,4
#               /       \           \
#              12,34    ...         ...
# so we can see that we have to solve 34 twice.
# 1. overlapped sub-problems
# As it is described above
# 2. the optimized sub-structure and state trasnformation:
# dp[i] shows the number of different decoding ways for s[0:i]
# dp[i] = dp[i-1] + dp[i-2] if 10<=s[i-1:i+2] <=26
# dp[i] = dp[i-1] else
