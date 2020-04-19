
# The key to this problem is fully understanding the description.
class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed))
        times = [(target-p)/s for p, s in cars]
        cnt = 0
        while len(times) > 1:
            lead = times.pop()
            # Per definition, a car can never pass another car ahead of it,
            # so, if a car cannot be caught by the one right after it, it will
            # never be caught
            if lead >= times[-1]:
                times[-1] = lead
            # If it can be caught, then the fleet will move on in the speed of leed
            else:
                cnt += 1
        return cnt + bool(times)
