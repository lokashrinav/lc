# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node):
            prev = None
            while node:
                saved = node.next
                node.next = prev
                prev = node
                node = saved
            return prev

        l1 = rev(l1)
        l2 = rev(l2)

        carryOne = 0
        dummy = ListNode(0)
        curr = dummy
        while l1 or l2:
            if not l1:
                calc = l2.val + 0 + carryOne
            elif not l2:
                calc = 0 + l1.val + carryOne
            else:
                calc = l2.val + l1.val + carryOne
            rem = 0
            if calc >= 10:
                rem = (calc - 10)
                carryOne = 1
            else:
                rem = calc 
                carryOne = 0
            curr.next = ListNode(rem)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        if carryOne:
            curr.next = ListNode(1)
        
        reversi2 = rev(dummy.next)
        
        return reversi2