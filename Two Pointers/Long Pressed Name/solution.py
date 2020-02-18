class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if name == typed:
            return True

        j = 0
        for c in name:
            if j == len(typed):
                return False

            if typed[j] != c:
                if j == 0 or typed[j-1] != typed[j]:
                    return False

                # discard all similar chars
                cur = typed[j]
                while j < len(typed) and typed[j] == cur:
                    j+=1
                if j == len(typed) or typed[j] !=c:
                    return False
            j+=1
        return True

# both the pointer of name and typed move forward until they mismatch
# Then for the pointer of typed, it continue to move forward until it meets with
# a new char, if that char is not the same as that of name, then return False 
