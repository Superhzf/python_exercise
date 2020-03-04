class Solution:
    def addStrings(self, num1: str, num2: str) -> str:


            dif = abs(len(num1)-len(num2))

            #make both strings same size
            if len(num1) > len(num2):

                num2 = ('0'*dif) + num2

            else:

                num1 = ('0'*dif) + num1


            N = len(num1)-1
            carry = 0
            result = ''
            while N >= 0:
                sums = int(num1[N]) + int(num2[N]) + carry
                # 8 + 9 =
                carry = sums//10
                result = str(sums%10) + result
                N-=1


            if carry == 1:
                return '1'+result

            return result
