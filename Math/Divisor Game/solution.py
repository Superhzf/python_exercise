# DP solution
class Solution:
    def divisorGame(self, N: int) -> bool:
        dp = [False for i in range(N+1)]
        for i in range(N+1):
             for j in range(1, i//2 + 1):
                    if i % j == 0 and (not dp[i - j]):
                        dp[i] = True
                        break
        return dp[N]


# Solution 2:
class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0
# Math proof:
# 1. If Alice starts with an even number she will always win.
# If Alice has an even number, she can always subtract 1, giving Bob an odd number.
# Odd numbers are not divisible by 2. They are only divisible by odd numbers.
# Hence Bob must subtract an odd number. Since odd minus odd is even,
# Bob will always return an even number to Alice. Alice will thus get a smaller
# even number after each round of play and Bob will get a smaller odd number
# after each round of play. Eventually Bob will have to play the number 1 and
# will lose the game since he will have no options.
# 2. If Alice starts with an odd number she will always lose.
# If Alice has an odd number, she has no choice but to subtract an odd
# number as odd numbers have no even divisors. Thus Bob will get an even number.
# Now using the argument from Part 1 above, Bob can take this even number and
# keep giving an odd number back to Alice by subtracting 1. Thus Bob will
# always get to play even and Alice will always be stuck with an odd number
# smaller than her previous odd number after each round. Eventually Alice will
# have to play the number 1 and will lose the game since she will have no options.
