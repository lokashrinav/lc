# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        hmap = defaultdict(int)

        while node:
            hmap[node.val] += 1
            node = node.next
        
        curr = head
        prev = None
        for key, val in hmap.items():
            curr.val = val
            prev = curr
            curr = curr.next

        if prev:
            prev.next = None
            
        return head