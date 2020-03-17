class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(i, curr): # i: starting point, curr: current list
            if i == len(S):
                perms.append("".join(curr))
                return

            if curr[i].isdigit():
                backtrack(i+1, curr)
            else:
                curr[i] = curr[i].upper()
                backtrack(i+1, curr)
                curr[i] = curr[i].lower()
                backtrack(i+1, curr)

        if len(S) == 0:
            return []

        perms = []
        curr = list(S)
        backtrack(0, curr)
        return perms

# I don't understand why the first parameter of backtrack always plus 1
# like backtrack(i+1,curr)
