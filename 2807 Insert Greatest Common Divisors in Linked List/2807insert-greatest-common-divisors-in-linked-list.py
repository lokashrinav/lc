# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        while node and node.next:
            saved = node.next
            node.next = ListNode(math.gcd(node.val, node.next.val))
            node.next.next = saved
            node = saved
        return head
        