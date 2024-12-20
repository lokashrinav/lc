# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        def rev(node):
            prev = None
            while node:
                saved = node.next
                node.next = prev
                prev = node
                node = saved
            return prev

        reversi = rev(head)

        count = 0 
        total = 0
        while reversi:
            if reversi.val == 1:
                total += (2 ** count)
                
            count += 1
            reversi = reversi.next
            
        return total



        