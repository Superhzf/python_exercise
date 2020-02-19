class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        def backtrack(i, cur):
            if i == len(S):
                perms.append("".join(cur))
                return

            if cur[i].isdigit():
                backtrack(i+1, cur)
            else:
                cur[i] = cur[i].upper()
                backtrack(i+1, cur)
                cur[i] = cur[i].lower()
                backtrack(i+1, cur)

        if not S:
            return []

        perms = []
        cur = list(S)
        backtrack(0, cur)
        return perms

# I don't understand why the first parameter of backtrack always plus 1
# like backtrack(i+1,cur)
