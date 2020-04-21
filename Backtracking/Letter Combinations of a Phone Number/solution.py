class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        def backtrack(curr_list, i, digit_list):
            if i == len(digit_list):
                res.append(''.join(curr_list))
                return

            candidates = mapping[digit_list[i]]
            curr_list[i] = candidates[0]
            backtrack(curr_list, i+1, digit_list)
            curr_list[i] = candidates[1]
            backtrack(curr_list, i+1, digit_list)
            curr_list[i] = candidates[2]
            backtrack(curr_list, i+1, digit_list)
            if digit_list[i] == '9' or digit_list[i] == '7':
                curr_list[i] = candidates[3]
                backtrack(curr_list, i+1, digit_list)

        res = []
        mapping = {'2':['a','b','c'],'3':['d','e','f'],'4':['g','h','i'],
                   '5':['j','k','l'],'6':['m','n','o'],'7':['p','q','r','s'],
                   '8':['t','u','v'],'9':['w','x','y','z']}
        if len(digits) == 0:
            return res
        digit_list = list(digits)
        curr_list = [None] * len(digits)
        backtrack(curr_list, 0, digit_list)
        return res

# I figured it out myself.
