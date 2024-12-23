# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        node = head
        connected = False
        while node:
            if node.val in s and not connected:
                connected = True
                ans += 1
            elif node.val not in s and connected:
                connected = False

            node = node.next
        
        return ans

        