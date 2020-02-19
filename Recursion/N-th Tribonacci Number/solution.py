class Solution:
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp_list = [0, 1, 1]
        for i in range(3, n+1):
            dp_list.append(dp_list[i-1] + dp_list[i-2] + dp_list[i-3])

        return dp_list[n]

# how to be faster than recursion
