class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        index = 0
        if len(str) == 0:
            return 0
        while index != len(str) and str[index] == ' ':
            index+=1
        if index == len(str):
            return 0

        negative = False
        #see if we have a sign
        if str[index] == '+':
            index+=1
        elif str[index] == '-':
            negative = True
            index+=1


        #now we check the rest of the string for numbers
        res = ''
        while index < len(str):
            if str[index] >= '0' and str[index] <= '9':
                res+=str[index]
            else:
                break
            index+=1

        if res is not '':
            integer = int(res)
            if negative is True:
                integer = 0-integer
        else:
            return 0

        if integer < 2**31-1 and integer > -2**31 :
            return integer
        elif integer >= 2*31-1:
            return 2**31-1
        elif integer <= -2**31:
            return -2**31

#
