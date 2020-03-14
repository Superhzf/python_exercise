#         1.Why carry is a&b:
#         If a and b are both 1 at the same digit, it creates one carry.
#         Because you can only use 0 and 1 in binary, if you add 1+1 together, it will roll that over to the next digit, and the value will be 0 at this digit.
#         if they are both 0 or only one is 1, it doesn't need to carry.

#         Use ^ operation between a and b to find the different bit
#         In my understanding, using ^ operator is kind of adding a and b together (a+b) but ignore the digit that a and b are both 1,
#         because we already took care of this in step1.


def getSum(self, a: int, b: int) -> int:
	carry = 0
    mask = 0xffffffff
    while b & mask != 0:
        carry = (a & b) << 1
        a = a ^ b
        b = carry

    # for overflow condition like
    # -1
    #  1
    return a&mask if b > mask else a


#more explanation about mask
# https://leetcode.com/problems/sum-of-two-integers/discuss/489210/Read-this-if-you-want-to-learn-about-masks

# Why we need a mask item?
# The reason is that in some situations (for example,a=-1,b=2), the carry
# item will never be 0. So, if the carry item is 100, the solution is to use number like 1000
# then 100&1000 = 0. The simpliest way is to use 0xffffffff because leetcode
# uses 32bit

# 原码
# 反码：若正数，则和原码一致；若负数，则符号位不变，原码其余各位取反
# 补码：若正数，则和原码一致；若负数，则将数字对应的反码加1
# 0的反码和补码均为0
