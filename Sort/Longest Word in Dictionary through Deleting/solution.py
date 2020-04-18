class Solution:
    def isSubString(self,s,d):
        if len(s) < len(d):
            return False
        if s == d:
            return True

        pos_s = 0
        pos_d = 0

        while pos_s < len(s):
            if pos_d == len(d):
                return True
            if s[pos_s] == d[pos_d]:
                pos_s += 1
                pos_d += 1
            else:
                pos_s += 1
        if pos_d == len(d):
            return True

        return False

    def findLongestWord(self, s: str, d: List[str]) -> str:
        word_candidate_list = []
        for this_d in d:
            if self.isSubString(s,this_d):
                word_candidate_list.append(this_d)

        if len(word_candidate_list) == 0:
            return ""

        longest_word = 0
        res = None
        for word in word_candidate_list:
            if len(word) > longest_word:
                longest_word = len(word)
                res = word
            elif len(word) == longest_word:
                if word < res:
                    res = word
        return res

# I figured out this problem myself
