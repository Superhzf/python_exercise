def plusOne(digits):
    digit_len = len(digits)

    if digits[-1] != 9:
        digits[-1] += 1
    elif digits == [9]*digit_len:
        return [1]+[0]*digit_len
    else:
        digits[-1] = 0
        count = digit_len - 1
        for digit in digits[n-2::-1]:
            if digit < 9:
                digits[count] = digits[count] + 1
                break
            else:
                digits[count] = 0
            count-=1
        return digits
