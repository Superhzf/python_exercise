class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(S):
            final_s = []
            skip = 0
            for s_char in reversed(S):
                if s_char == '#':
                    skip += 1
                elif skip > 0:
                    skip-=1
                else:
                    final_s.append(s_char)
            return final_s


        final_s = F(S)
        final_t = F(T)

        if len(final_s)!=len(final_t):
            return False

        for s,t in zip(final_s,final_t):
            if s != t:
                return False
        return True

# The idea to find the final string is
# iterate in a reversed order and skip char after #
# two pointers, s_char and skip here
