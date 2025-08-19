# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

        hset = set()
        rep = set()

        node = head
        while node:
            if node.val in hset:
                rep.add(node.val)
            hset.add(node.val)
            node = node.next
        
        node = head
        prev = None
        while node:
            if node.val in rep:
                if prev is None:
                    head = node.next
                else:
                    prev.next = node.next
            else:
                prev = node
            node = node.next
        
        return head

