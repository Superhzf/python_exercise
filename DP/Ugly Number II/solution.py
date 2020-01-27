class Solution:
    def nthUglyNumber(self, n: int) -> int:

        ugly_num_list = [0]*n

        ugly_num_list[0] = 1
        # ugly_num_list 中的数是有2，3，5不断的和2，3，5以及他们的乘积再相乘得到的
        # 每一个ugly number都是上述乘积集中，比上个ugly number大的最小的数
        # i2表示ugl_num_list中最近一次和2相乘的ugly number的坐标
        i2 = 0
        i3 = 0
        i5 = 0

        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        for i in range(1,n):
            ugly_num_list[i] = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)

            if ugly_num_list[i] == next_multiple_of_2:
                i2 += 1
                next_multiple_of_2 = ugly_num_list[i2] * 2

            if ugly_num_list[i] == next_multiple_of_3:
                i3 += 1
                next_multiple_of_3 = ugly_num_list[i3] * 3

            if ugly_num_list[i] == next_multiple_of_5:
                i5 += 1
                next_multiple_of_5 = ugly_num_list[i5] * 5

        return ugly_num_list[-1]
# 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
