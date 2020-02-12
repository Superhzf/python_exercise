# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        d={}
        while headA:
            d[headA] = 1
            headA = headA.next

        while headB:
            if headB in d:
                return headB
            headB=headB.next

# the idea is to traverse list A and store the address/reference to each node
# in a hash set. Then check every node bi in list B: if bi appears in the hash set,
# then bi is the intersection node.

# I did not realize that the hash set can be created like this
