# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy2 = ListNode(0)

        curr1, curr2 = dummy1, dummy2

        node = head
        count = 0
        while node:
            if count % 2:
                curr2.next = node
                curr2 = curr2.next
            else:
                curr1.next = node
                curr1 = curr1.next
            count += 1
            node = node.next
        curr1.next = None
        curr2.next = None
            
        curr1.next = dummy2.next
        return dummy1.next

        
        