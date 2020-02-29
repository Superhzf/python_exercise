# The main idea is to count the 1s and 0s in the binary representation of number.
# if there is only one 1 and an even number of zeros that means it is a power of four:

class Solution:
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        counts1 = 0
        counts0 = 0
        if num>0:
            while num!=0:
                counts1 += num&1
                if (num|0) != 1:
                    counts0+=1
                num >>= 1
        return (counts1==1 and counts0 % 2 == 0)
