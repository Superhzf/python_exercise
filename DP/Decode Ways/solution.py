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

# for example s ='123'
# The idea is that we start from the left,
# 已知'1'只有一种情况
# ‘12’ 有1,2和12两种情况
# '123'的结果基于上面的两种情况，将12视为一个整体，3自己一个整体；将23视为一个整体
# number_decode[i] shows that how many decoding methods are for s[:i-1]
