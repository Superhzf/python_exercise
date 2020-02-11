class Solution:
    def isHappy(self, n: int) -> bool:

        hash_dict = set()
        while True:

            sq = 0
            while n:
                last_digit = n%10
                sq += last_digit*last_digit
                n = int(n/10)

            n = sq

            if sq == 1:
                return True

            if sq in hash_dict:
                return False
            else:
                hash_dict.add(sq)

# The idea is that using hash table to store visited numbers
# if the sum of squares have showed up before, then return false
