class Solution:
    def toHex(self, num: int) -> str:
        mapping = {0: '0', 0: '0', 1: '1', 2: '2', 3: '3', 4: '4',5:'5',6:'6',
                   7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b', 12: 'c', 13: 'd',
                   14: 'e', 15: 'f'}

        if num == 0:
            return '0'
        if num<0:
            num = num & (2**32-1) # The reason for this is that it will convert
                                  # the negative number to corresponding
                                  # positive number after removing the sign
                                  # based on two's complement
        res = ''
        while num > 0:
            res =  mapping[num%16] + res
            num = num//16
        return res
