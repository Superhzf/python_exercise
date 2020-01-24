def intersect(nums1, nums2):
    nums1_dict = {}
    nums2_dict = {}
    intersection = []

    for num1 in nums1:
        if num1 in nums1_dict.keys():
            nums1_dict[num1] = nums1_dict[num1] + 1
        else:
            nums1_dict[num1] = 1

    for num2 in nums2:
        if num2 in nums2_dict.keys():
            nums2_dict[num2] = nums2_dict[num2] + 1
        else:
            nums2_dict[num2] = 1

    for key in nums2_dict.keys():
        if key in nums1_dict.keys():
            common = min(nums1_dict[key],nums2_dict[key])
            for _ in range(common):
                intersection.append(key)
    return intersection
