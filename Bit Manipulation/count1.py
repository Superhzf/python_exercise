# Question is how to count number of 1s in an integer
def countBits(num:int) -> int:
    count = 0
    while num != 0:
        count = count + (num & 1)
        num = num >> 1
    return count
