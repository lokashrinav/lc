# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        count = 0
        prev = None
        node = head

        while node:
            count = count % (m + n)
            if count >= m and count < (m + n):
                node = node.next
            else:
                if prev:
                    prev.next = node

                prev = node
                node = node.next
                
            count += 1

        if prev:
            prev.next = None
        
        return head
