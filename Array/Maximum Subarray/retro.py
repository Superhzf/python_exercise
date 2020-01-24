def maxSubArray(nums):
    current_sum = nums[0]
    best_sum = [0]
    for num in nums[1:]:
        current_sum = max(num,current_sum+num)
        best_sum = max(current_sum,best_sum)
    return best_sum
