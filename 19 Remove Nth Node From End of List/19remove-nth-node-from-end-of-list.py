# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node1 = head
        count = 0
        while node1:
            node1 = node1.next
            count += 1
        
        k = count - n
        node = head

        prev = None
        count = 0
        while node:
            if count == k:
                if prev:
                    prev.next = node.next
                else:
                    head = head.next

            count += 1
            prev = node
            node = node.next
        
        return head