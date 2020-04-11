from itertools import groupby
class Solution:
    def expressiveWords(S: str, words: List[str]) -> int:
        def RLE(S):
            res = []
            for label, group in groupby(S):
                res.append((label,len(list(group))))
            return zip(*res)

        R, count = RLE(S)
        res = 0
        for word in words:
            this_word, this_count = RLE(word)
            if this_word != R:
                continue
            if all(c1 == c2 or c1 >= max(3, c2) for c1, c2 in zip(count, this_count)):
                    res += 1
        return res
