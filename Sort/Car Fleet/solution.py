class Solution:

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            # Per definition, a car can never pass another car ahead of it,
            # so, if a car cannot be caught by the one right after it, it will
            # never be caught
            if lead < times[-1]:
                ans += 1
            # If it can be caught, then the fleet will move on in the speed of leed
            else: times[-1] = lead

        return ans + bool(times) # remaining car is fleet (if it exists)

# The key to this problem is fully understanding the description.
