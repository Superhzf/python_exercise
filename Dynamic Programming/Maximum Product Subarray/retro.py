def maxProduct(nums):
    if len(nums) == 0:
        return
    if len(nums) == 1:
        return nums[0]

    res, curr_max, curr_min = nums[0],nums[0],nums[0]
    for i in range(1,len(nums)):
        this_max = max(curr_max*nums[i],curr_min*nums[i],nums[i])
        this_min = min(curr_max*nums[i],curr_min*nums[i],nums[i])
        curr_max = this_max
        curr_min = this_min

        res = max(curr_max,res)
    return res
