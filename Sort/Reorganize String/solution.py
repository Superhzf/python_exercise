class Solution:
    def reorganizeString(self, S: str) -> str:
        N = len(S)
        A = []
        hash_map = {}
        for char in S:
            if char in hash_map:
                hash_map[char] += 1
                if hash_map[char] > (N+1)/2:
                    return ""
            else:
                hash_map[char] = 1
        A = []
        # The elements that happen the most time should be put in the front
        for key,value in sorted([(key,value) for key,value in hash_map.items()],key=lambda x:x[1],reverse=True):
            A = A + [key] * value
        ans = [None] * N
        pos = 0
        for i in range(0,N,2):
            ans[i] = A[pos]
            pos += 1
        for j in range(1,N,2):
            ans[j] = A[pos]
            pos += 1
        return "".join(ans)
