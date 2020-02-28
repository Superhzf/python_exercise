class Solution:
    def removeDuplicates(self, S: str) -> str:

        result = ""

        for c in S:
            if(not result):
                result += c
                continue

            if(result[-1] == c):
                result = result[:-1]
            else:
                result += c

        return result

# it is a typical stack implementation
