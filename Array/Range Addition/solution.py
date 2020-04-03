class Solution:
    def getModifiedArray(self, length, updates):
        arr = [0] * (length + 1)
        for start, end, inc in updates:
            arr[start] += inc
            arr[end+1] -= inc
        for i in range(1, length+1):
            arr[i] = arr[i] + arr[i-1]
        return arr[:-1]

# This solution will be easier to understand by drawing a picture in a draft
