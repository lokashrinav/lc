# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        node = head
        count = 0
        last = node
        while node:
            count += 1
            last = node
            node = node.next

        remainder = count - (k % count)
        last.next = head

        node = head
        prev = node
        while remainder:
            prev = node
            node = node.next
            remainder -= 1
        prev.next = None
        return node


        


        