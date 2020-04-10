class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ','')
        while True:
            index_mult = s.find('*')
            index_div = s.find('/')

            if index_mult != -1 and index_div != -1:
                if index_mult < index_div:
                    this_index = index_mult
                elif index_div < index_mult:
                    this_index = index_div
            elif index_mult == -1 and index_div == -1:
                break
            elif index_mult == -1:
                this_index = index_div
            else:
                this_index = index_mult


            right = this_index+1
            left = this_index - 1
            while right < len(s) and s[right].isdigit():
                right += 1
            while left >= 0 and s[left].isdigit():
                left -= 1

            if this_index == index_mult:
                if right == len(s) - 1:
                    this_res = int(s[left+1:this_index])*int(s[this_index+1:])
                else:
                    this_res = int(s[left+1:this_index])*int(s[this_index+1:right])
            else:
                if right == len(s) - 1:
                    this_res = int(s[left+1:this_index])//int(s[this_index+1:])
                else:
                    this_res = int(s[left+1:this_index])//int(s[this_index+1:right])

            s = s[:left+1] + str(this_res) + s[right:]


        try:
            s = int(s)
            return s
        except:
            res = 0
            total_minus = 0
            for plus_split in s.split('+'):
                if '-' in plus_split:
                    for index,minus_split in enumerate(plus_split.split('-')):
                        if index == 0:
                            total_minus = int(minus_split)
                        else:
                            total_minus -= int(minus_split)
                else:
                    total_minus += int(plus_split)
                res += total_minus
                total_minus = 0
            return res
# Above is my solution
# Below is a better solution from the community
class Solution:
    def calculate(self, s: str) -> int:
            s = s.replace(' ','')
            num = 0
            res = 0
            pre_op = '+'
            s+='+'
            stack = []
            for c in s:
                if c.isdigit():
                    num = num*10 + int(c)
                else:
                    if pre_op == '+':
                        stack.append(num)
                    elif pre_op == '-':
                        stack.append(-num)
                    elif pre_op == '*':
                        operant = stack.pop()
                        stack.append((operant*num))
                    elif pre_op == '/':
                        operant = stack.pop()
                        stack.append(math.trunc(operant/num))
                    num = 0
                    pre_op = c
            return sum(stack)
