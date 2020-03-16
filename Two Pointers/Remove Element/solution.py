class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        char = 0 # it points to the position of val
        for d in range(len(nums)):
            if nums[d] != val:
                nums[char] = nums[d]
                char+=1
        return char
