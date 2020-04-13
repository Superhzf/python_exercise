class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = 0
        hi = 0
        for c in s:
            if c == '(':
                lo += 1
                hi += 1
            elif c == ')':
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1

            if hi < 0:
                # If hi < 0, it means there is a ')' and does not have a
                # corresponding '('
                return False

            lo = max(0,lo)

        return lo == 0

# idea:
# When checking whether the string is valid, we only cared about the "balance":
# the number of extra, open left brackets as we parsed through the string.
# For example, when checking whether '(()())' is valid, we had a balance of 1, 2, 1, 2, 1, 0
# as we parse through the string: '(' has 1 left bracket, '((' has 2, '(()' has 1,
# and so on. This means that after parsing the first i symbols, (which may include asterisks,)
# we only need to keep track of what the balance could be.

# lo: the smallest number of open left brackets after processing the current character in the string.
# hi: the largest number of open left brackets after processing the current character in the string.
