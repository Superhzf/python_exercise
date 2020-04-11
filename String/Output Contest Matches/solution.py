class Solution:
    def findContestMatch(self, n: int) -> str:
        team = list(map(str, range(1, n+1)))
        while n > 1:
            for i in range(n//2):
                team[i] = "({},{})".format(team[i],team.pop())
            n = n//2

        return team[0]

# One thing that is worth noticing is that we may have to
# consider several games as one game
