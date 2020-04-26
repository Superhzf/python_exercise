class Solution:
    def __init__(self):
        self.max_len = 0

    def maxLength(self, arr: List[str]) -> int:

        def backtrack(first=0):
            curr_str = ''.join(curr_list)
            if len(curr_str) == len(set(curr_str)):
                self.max_len = max(self.max_len, len(curr_str))

            for curr_pos in range(first, len(arr)):
                curr_list.append(arr[curr_pos])
                backtrack(curr_pos + 1)
                curr_list.pop()

        curr_list = []
        backtrack()
        return self.max_len
