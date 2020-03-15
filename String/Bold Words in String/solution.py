class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
        #mark bold char
        mark = [False]*len(S) #true for bold char
        for word in words:
            i = -1
            while True:
                i = S.find(word, i+1)
                if i == -1:
                    break
                # mask[i] = true if and only if the i-th letter is bold
                for j in range(i, i+len(word)):
                    mark[j] = True
        #insert tags
        ans = []
        for i in range(len(S)):
            if mark[i] and (i == 0 or not mark[i-1]):
                ans.append("<b>")
            ans.append(S[i])
            if mark[i] and (i == len(S) - 1 or not mark[i+1]): ans.append("</b>")
        return "".join(ans)
