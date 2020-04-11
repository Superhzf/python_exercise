class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for i,x,y in sorted(zip(indexes, sources, targets), reverse=True):
            if S[i:].startswith(x):
                S = S[:i] + y + S[i+len(x):]
        return S

# The key here is that we do in reversed order so that
# the indexes would alwasy work
