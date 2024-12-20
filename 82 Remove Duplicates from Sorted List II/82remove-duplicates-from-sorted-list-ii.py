# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        hmap = {}
        hmap[head.val] = 1
        node = head

        while node and node.next:
            if node.next.val in hmap:
                hmap[node.next.val] += 1
            else:
                hmap[node.next.val] = 1
            node = node.next

        node = head

        while node and hmap[node.val] > 1:
            node = node.next
            head = node
        
        if not node:
            return None

        while node and node.next:
            if hmap[node.next.val] > 1:
                node.next = node.next.next
            else:
                node = node.next
        
        return head

        