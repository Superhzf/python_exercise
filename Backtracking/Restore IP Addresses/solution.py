class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def valid(segment):
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def backtrack(prev_pos=-1, dots=3):
            if dots == -1:
                output.append('.'.join(segments))
                return
            else:
                if dots > 0:
            # The current dot curr_pos could be placed
            # in a range from prev_pos + 1 to prev_pos + 4.
            # The dot couldn't be placed
            # after the last character in the string.
                    for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                        segment = s[prev_pos+1:curr_pos+1]
                        if valid(segment):
                            segments.append(segment)
                            backtrack(curr_pos, dots-1)
                            segments.pop()
                else:
                    segment = s[prev_pos + 1:]
                    if valid(segment):
                        segments.append(segment)
                        backtrack(prev_pos, dots-1)
                        segments.pop()
        n = len(s)
        output = []
        segments = []
        backtrack()
        return output

# time complexity: O(1) because there are less than 27 possibilities to check
# space: O(1), there are less than 19 valid IP addresses to keep
