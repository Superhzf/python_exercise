# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3_next = ListNode(None)
        l3 = l3_next
        while l1 or l2:
            if l1 and l2:
                if l1.val<l2.val:
                    l3_next.next = l1
                    l1 = l1.next
                else:
                    l3_next.next = l2
                    l2 = l2.next
            elif l1:
                l3_next.next = l1
                l1 = l1.next
            else:
                l3_next.next = l2
                l2 = l2.next
            l3_next = l3_next.next
        return l3.next

# The problem here is how to append next node to l3
# The idea is that we use two node objects l3 and l3_next, l3 is the head node
# while l3_next is always pointing to the last node.
