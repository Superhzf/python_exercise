class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        size = len(height)
        l = 0
        r = size - 1
        while l < r:
            this_area = min(height[l],height[r]) * (r-l)
            if this_area > max_area:
                max_area = this_area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area

# The idea is that the area is determined by the lower container, so we just have
# to find the lower one
# Step 1: start from left = 0 and right = len(height) - 1
# Step 2: calculate the area
# Step 3: if height[l] < height[r], move l to the right, otherwise move r to the left
