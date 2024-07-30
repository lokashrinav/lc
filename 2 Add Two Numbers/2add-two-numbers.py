# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(0)
        carry = 0
        while l1 or l2:
            if not l1: 
                l1_val = 0 
            else: 
                l1_val = l1.val

            if not l2: 
                l2_val = 0 
            else: 
                l2_val = l2.val
                
            add = l1_val + l2_val + carry
            carry = 0
            if add >= 10:
                add = add - 10
                carry = 1
            dummy.next = ListNode(add)
            dummy = dummy.next
            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next 

        if carry:
            dummy.next = ListNode(1)
        return head.next
            

        