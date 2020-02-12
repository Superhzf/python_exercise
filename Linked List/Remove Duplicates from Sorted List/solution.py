# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = ListNode(0)
        curr = head
        if not curr:
            return head
        prev = curr
        curr = curr.next
        while curr:
            if prev.val == curr.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return head

# The key is if we want to drop a node, how to make it's previous node
# connect to it's next one?
