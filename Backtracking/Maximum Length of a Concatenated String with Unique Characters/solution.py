class Solution:
    def __init__(self):
        self.max_len = 0

    def maxLength(self, arr: List[str]) -> int:

        def backtrack(curr_list=[],index=0):
            curr_str = ''.join(curr_list)
            if len(curr_str) == len(set(curr_str)):
                self.max_len = max(self.max_len,len(curr_str))

            for i in range(index,len(arr)):
                curr_list.append(arr[i])
                backtrack(curr_list, i+1)
                curr_list.pop()

        backtrack()
        return self.max_len
