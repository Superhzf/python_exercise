def moveZeroes(nums):
    if len(nums) == 0:
        return

    if len(nums) == 1:
        reurn nums

    LastZeroFoundAt = 0
    for index,num in enumerate(nums):
        if num != 0:
            nums[index],nums[LastZeroFoundAt] = nums[LastZeroFoundAt],nums[index]
            LastZeroFoundAt+=1
