def nthUglyNumber(n):
    ugly_num_list = [0]*n
    ugly_num_list[0] = 1

    i2 = 0
    i3 = 0
    i5 = 0

    next_multiple_of_2 = 2
    next_multiple_of_3 = 3
    next_multiple_of_5 = 5
    for i in range(1,n):
        ugly_num_list[i] = min(next_multiple_of_2,next_multiple_of_3,next_multiple_of_5)

        if ugly_num_list[i] == next_multiple_of_2:
            i2 += 1
            next_multiple_of_2 = ugly_num_list[i2]*2

        if ugly_num_list[i] == next_multiple_of_3:
            i3+=1
            next_multiple_of_3 = ugly_num_list[i3]*3

        if ugly_num_list[i] == next_multiple_of_5:
            i5+=1
            next_multiple_of_5 = ugly_num_list[i5]*5

    return ugly_num_list[-1]
