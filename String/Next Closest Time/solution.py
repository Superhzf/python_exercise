class Solution:
    def nextClosestTime(self, time: str) -> str:
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            if all(digit in allowed
                    for block in divmod(cur, 60)
                    for digit in divmod(block, 10)):
                return "{:02d}:{:02d}".format(*divmod(cur, 60))

# The idea is :
# cur: current time by minutes
# we repeatedly find the next time by minutes and test whether the next
# time is valid
