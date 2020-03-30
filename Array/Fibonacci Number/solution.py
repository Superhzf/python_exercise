class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        if N == 1:
            return 1

        # Solution 1
        # return self.fib(N-1) + self.fib(N-2)
        # Solution 2
        fib_list=[0,1]
        for i in range(2,N):
            fib_list.append(fib_list[i-1] + fib_list[i-2])

        return fib_list[-1]+fib_list[-2]


# I figured out two solutions myself.
# I'm proud of myself so I write them down
