class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        flag = 0
        pos = 0
        for i in range(length - 1):
        	if nums[i] > nums[i + 1]:
        		if flag == 0:
        			flag = 1
        			pos = i
        		else:
        			return False
        if flag == 0:
        	return True
        if length == pos + 2 or pos == 0:
        	return True
        # After iteration, we have to check this
        if nums[pos-1] <= nums[pos+1] or nums[pos] <= nums[pos+2]:
        	return True
        return False
