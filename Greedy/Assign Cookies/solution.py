class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        p_g = 0
        p_s = 0

        while p_g < len(g) and p_s < len(s):
            if g[p_g] <= s[p_s]:
                p_g += 1
            p_s += 1

        return p_g
