# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        hmap = {}
        hmap[0] = dummy
        node = head
        preSum = 0
        dummy.next = head
        while node:
            preSum += node.val
            if preSum in hmap:
                removal = hmap[preSum].next
                fun = preSum
                while removal and removal != node:
                    fun += removal.val
                    del hmap[fun]
                    removal = removal.next
                hmap[preSum].next = node.next
            else:
                hmap[preSum] = node
            node = node.next
        return dummy.next
        