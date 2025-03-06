# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:

        def rev(node):
            prev = None
            while node:
                saved = node.next
                node.next = prev
                prev = node
                node = saved
            return prev
            
        node = idk = rev(head)

        carry = 1
        prev = None

        while node and carry:
            if node.val + carry >= 10:
                node.val = 0
                carry = 1
            else:
                node.val += carry
                carry = 0

            prev = node
            node = node.next

        
        if carry:
            newNode = ListNode(carry)
            prev.next = newNode
        
        head = rev(idk)
        
        return head
