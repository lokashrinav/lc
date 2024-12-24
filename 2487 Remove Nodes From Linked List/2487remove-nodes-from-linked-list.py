# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node):
            prev = None
            while node:
                saved = node.next
                node.next = prev
                prev = node
                node = saved
            return prev
        reversi = rev(head)
        maxNum = 0
        prevNode = None
        head = reversi
        while reversi:
            if reversi.val >= maxNum:
                maxNum = reversi.val
                prevNode = reversi
            else:
                prevNode.next = reversi.next
            reversi = reversi.next

        return rev(head)

        
        
        
        