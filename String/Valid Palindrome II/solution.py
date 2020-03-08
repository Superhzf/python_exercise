class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s == s[::-1]:
            return True
        for i in range(len(s)-1):
            if s[i] != s[-i-1]:
                return s[i: -i-2] == s[i+1: -i-1][::-1] or s[i+1: -i-1] == s[i+2: len(s)-i][::-1]
        return False
