class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)
        # i, j: negative, positive parts
        pos = 0

        res = []
        while pos<N and A[pos]<0:
            pos += 1
        neg = pos -1

        while neg>=0 and pos<=N-1:
            if A[neg]*A[neg]<A[pos]*A[pos]:
                res.append(A[neg]*A[neg])
                neg-=1
            else:
                res.append(A[pos]*A[pos])
                pos+=1

        while pos<=N-1:
            res.append(A[pos]*A[pos])
            pos+=1
        while neg>=0:
            res.append(A[neg]*A[neg])
            neg-=1

        return res
