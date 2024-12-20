# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(head):
            prev = None
            node = head
            while node:
                saved = node.next
                node.next = prev
                prev = node
                node = saved
            return prev
            # 4 -> 5 -> 6

        reversi = rev(head)
        
        carryOne = 0
        dummy = ListNode(0)
        curr = dummy
        while reversi:
            calc = reversi.val + reversi.val + carryOne
            rem = 0
            if calc >= 10:
                rem = (calc - 10)
                carryOne = 1
            else:
                rem = calc
                carryOne = 0
            curr.next = ListNode(rem)
            curr = curr.next
            reversi = reversi.next

        if carryOne:
            curr.next = ListNode(1)
        return rev(dummy.next)
            

                