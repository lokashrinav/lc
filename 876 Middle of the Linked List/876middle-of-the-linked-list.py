# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        turtle, hare = head, head
        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
        
        return turtle
        