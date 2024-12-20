# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set(nums)
        node = head
        prev = None
        while node and node.val in num_set:
            node = node.next
        
        if not node:
            return None
        head = node
        prev = None

        while node:
            if node.val in num_set:
                prev.next = node.next
                node = node.next
            else:
                prev = node
                node = node.next

        return head
            
        