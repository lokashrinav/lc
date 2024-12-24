# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        
        turtle, hare = head, head
        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            if turtle == hare:
                break
        
        if not hare or not hare.next: return None

        turtle = head
        while turtle != hare:
            turtle = turtle.next
            hare = hare.next
        
        return turtle
        