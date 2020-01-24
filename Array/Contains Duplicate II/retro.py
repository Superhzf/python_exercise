def containsNearbyDuplicate(nums,k):
    num_index_dict = {}
    for index,value in enumearte(nums):
        if value not in num_index_dict.values():
            num_index_dict[value] = index
        else:
            if index - num_index_dict[value] <= k:
                return True
            else:
                num_index_dict[value] = index # update the dict
    return False
