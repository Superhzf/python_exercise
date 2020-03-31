
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cap = 0
        if 1 in flowerbed:
            first_one = flowerbed.index(1)
            if first_one >= 2:
                cap = cap + (first_one-1)/2
                if cap//1 != cap:
                    cap = int(cap) + 1
                else:
                    cap = int(cap)
            flowerbed = flowerbed[first_one:]
        else:
            cap = len(flowerbed)/2
            if cap//1 != cap:
                cap = int(cap) + 1
            else:
                cap = int(cap)
            return cap>=n

        last_one = flowerbed[::-1].index(1)

        if last_one >= 2:
            cap = cap + (last_one-1)/2
            if cap//1 != cap:
                cap = int(cap) + 1
            else:
                cap = int(cap)
        flowerbed = flowerbed[::-1][last_one:][::-1]

        if 1 in flowerbed:
            for label,group in itertools.groupby(flowerbed):
                this_group = list(group)
                if label == 0 and len(this_group) >=3:
                    cap += (len(this_group)-2)/2
                    if cap//1 != cap:
                        cap = int(cap) + 1
                    else:
                        cap = int(cap)

        return cap>=n

# I figured out this problem myself
# Things that are worth to notice is "this_group = list(group)"
