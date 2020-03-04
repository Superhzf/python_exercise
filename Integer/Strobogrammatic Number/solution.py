class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
            graph = {"1":"1", "6":"9", "8":"8", "9":"6", "0":"0"}
            cmp = ""
            for c in num:
                if c in graph:
                    cmp += graph[c]
                else: return False
            return cmp[::-1] == num
