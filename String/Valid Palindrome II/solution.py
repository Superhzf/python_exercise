class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2+1):
            if s[i] != s[~i]:
                return s[i+1:n-i] == s[i+1:n-i][::-1] or s[i:~i] == s[i:~i][::-1]
        return True  
