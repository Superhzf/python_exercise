class Solution:

    def searchRange(self, nums, target):

        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1, -1]

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left = mid
                right = mid
                while left >=0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1

                return [left + 1, right - 1]

            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

        return [-1, -1]
