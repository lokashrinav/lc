# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        turtle, hare = head, head.next
        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next

        saved = turtle.next
        turtle.next = None

        def rev(head):
            prev = None
            node = head
            while node:
                saved = node.next
                node.next = prev
                prev = node
                node = saved
            return prev

        reversi = rev(saved)
        
        maxSum = 0
        while reversi:
            maxSum = max(reversi.val + head.val, maxSum)
            head = head.next
            reversi = reversi.next
        
        return maxSum


        