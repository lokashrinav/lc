# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = head
        while node and node.next:
            if node == head:
                head = node.next
                node.next = node.next.next
                head.next = node
            else:
                saved = node.next
                node.next = node.next.next
                saved.next = node
                prev.next = saved
            prev = node
            node = node.next
        return head


        