# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        turtle, hare = head, head.next
        while hare and hare.next:
            turtle = turtle.next
            hare = hare.next.next
        head2 = turtle.next
        turtle.next = None
        
        node2 = head2
        prev = None
        while node2:
            saved = node2.next
            node2.next = prev
            prev = node2
            node2 = saved
            
        
        head2 = prev
        
        while head and head2:
            if head.val != head2.val:
                return False
            head = head.next
            head2 = head2.next
        
        return True
        
            
        
        