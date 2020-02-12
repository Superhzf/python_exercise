# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

# Assume that we have linked list 1 → 2 → 3 → Ø, we would like to change it to Ø ← 1 ← 2 ← 3.

# While you are traversing the list, change the current node's next pointer to
# point to its previous element.
# Since a node does not have reference to its previous node,
# you must store its previous element beforehand.
# You also need another pointer to store the next node before changing the reference.
# Do not forget to return the new head reference at the end!
