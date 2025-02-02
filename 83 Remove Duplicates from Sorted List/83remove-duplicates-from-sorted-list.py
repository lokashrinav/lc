# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node = head
        prev = None

        while node:
            if prev and prev.val == node.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        
        return head
        