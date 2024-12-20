# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        first = k - 1
        second = count - k

        node1, node2 = head, head
        while first:
            node1 = node1.next
            first -= 1
        
        while second:
            node2 = node2.next
            second -= 1
        
        node1.val, node2.val = node2.val, node1.val

        return head
        