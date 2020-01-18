class Solution:

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return s
        pali_index = []
        longest_pali = s[0]

        for j in range(len(s)):
            pali_index.append((j,j))
            longest_pali = s[j]

        for i in range(1,len(s)):
            if s[i-1] == s[i]:
                pali_index.append((i-1,i))
                longest_pali = s[i-1:i+1]


        max_len = len(longest_pali)
        for i,j in pali_index:
            left = i
            right = j
            while left-1>=0 and right+1<=len(s)-1 and s[left-1] == s[right+1]:
                left-=1
                right+=1
            if right - left + 1 > max_len:
                max_len = right - left + 1
                longest_pali = s[left:right+1]

        return longest_pali

# This is a classic DP problem
# we start from the basic problem which is the len of sub palindrome is one or two letters,say P(i,j), j = i or j = i+1
# Then, if s[i-1] == s[j+1], then s[i-1:j+1] is a palindrome
