# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True

        if not head.next:
            return True

        slow = head
        fast = head

        # now slow is the middle node if the len is odd
        # or the start of the second half of the linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # reverse the second half

        # slow is the start of the second half of the linked list
        if fast:
            middle = slow
            slow = slow.next

        # reverse the second half
        curr = slow
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # compare the first half and the second half
        while prev:
            if prev.val != head.val:
                return False

            prev = prev.next
            head = head.next
        return True

# 1) Get the middle of the linked list.
# 2) Reverse the second half of the linked list.
# 3) Check if the first half and second half are identical.
# 4) Construct the original linked list by reversing the second half again and attaching it back to the first half
