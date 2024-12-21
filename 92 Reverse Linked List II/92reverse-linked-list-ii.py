# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        node = head
        count = 1
        prev = None
        saved_prev = None
        first = None
        if left == right:
            return head

        while node:
            if left <= count <= right:
                if count == left:
                    saved_prev = prev
                    saved = node.next
                    first = node
                    prev = node
                    node.next = None
                    node = saved
                elif count == right:
                    saved = node.next
                    node.next = prev
                    if saved_prev:
                        saved_prev.next = node
                    else:
                        head = node
                    first.next = saved
                    node = saved
                else:
                    saved = node.next
                    node.next = prev
                    prev = node
                    node = saved
            else:
                prev = node
                node = node.next

            count += 1

        return head