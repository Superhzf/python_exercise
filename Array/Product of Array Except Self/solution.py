class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        answer[0] = 1
        for i in range(1,length):
            answer[i] = nums[i-1] * answer[i-1]

        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i]*R
            R = R * nums[i]

        return answer

# The idea is building two arrays LEFT and RIGHT,
# LEFT[i] contains the product of all elements to the left of i
# RIGHT[i] contains the product of all elements to the right of i
