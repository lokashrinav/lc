# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        turtle, hare = head, head
        prev = None
        while hare and hare.next:
            prev = turtle
            turtle = turtle.next
            hare = hare.next.next
        
        node = head
        if prev:
            prev.next = turtle.next
        else:
            head = turtle.next

        return head
        