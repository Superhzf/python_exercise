class Solution:
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    def reverse_each_word(self, l: list) -> None:
        n = len(l)
        start = 0
        end = 0

        while start < n:
            while end < n and l[end] != ' ':
                end += 1

            self.reverse(l, start, end - 1)
            start = end + 1
            end += 1

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reverse(s, 0, len(s) - 1)

        self.reverse_each_word(s)

# The idea is
# reverse the list and reverse each word
