# the basic solution sort and find the least element each time which is slow
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        while K>0:
            for j in range(0,n-1):
                if A[j] < A[j+1]:
                    A[j],A[j+1] = A[j+1],A[j]
            A[-1] = A[-1]*-1
            K-=1
        return sum(A)

# this method consider the negative and positive elements separately
class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        A = sorted(A)
        neg = [i for i in A if i < 0]
        pos = [i for i in A if i >= 0]
        res =[]
        for i in neg:
            if K:
                res.append(i*-1)
                K-=1
            else:
                res.append(i)

        res = sorted(res + pos)
        if K % 2 == 1:
            res[0]*= -1

        return sum(res)
