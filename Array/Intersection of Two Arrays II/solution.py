class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_dic = {}
        nums2_dic = {}
        intersect = []

        for i in range(len(nums1)):
            num = nums1[i]
            if num in nums1_dic:
                nums1_dic[num] += 1 #increases the value by 1 if same number appears in the array
            else:
                nums1_dic[num] = 1 #Sets the value to 1 for the first appearance of the number in the array


        for j in range(len(nums2)):
            num2 = nums2[j]
            if num2 in nums2_dic:
                nums2_dic[num2] += 1 #increases the value by 1 if same number appears in the array
            else:
                nums2_dic[num2] = 1 #Sets the value to 1 for the first appearance of the number in the array


        for key in nums1_dic.keys(): #Goes through every key in the dictionary
            if key in nums2_dic.keys(): # Looking for a matched key in the second array
                common = min(nums1_dic[key],nums2_dic[key]) # The minimum time this number appears between these two arrays should be the number of time the number(say 2) appears in both arrays
                for k in range(common):
                    intersect.append(key) # adding the key (say 2), as many times it appears in both array (which should be = common)

        return intersect
