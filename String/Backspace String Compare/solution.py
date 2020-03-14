# Solution 1
# Space compleity is O(M+N)
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def CalculateFinalString(S:str) -> str:
            stack = []

            for char in S:
                if char != '#':
                    stack.append(char)
                else:
                    if len(stack)>0:
                        stack.pop()
                    else:
                        continue

            return ''.join(stack)

        final_s = CalculateFinalString(S)
        final_t = CalculateFinalString(T)

        return final_s == final_t


# Solution 2
# The idea is to use two pointers, that way the space complexity is O(1)
