class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return x
        if x<=2:
            return 1

        l = 1
        r = x

        while l<=r:
            middle = (l+r)//2

            if x>=middle*middle and x<(middle+1)*(middle+1):
                return middle
            elif x<middle*middle:
                r = middle-1
            else:
                l = middle+1

# The key here is when to stop: when x>=middle*middle and x<(middle+1)*(middle+1)
