# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        dummy2 = ListNode(0)
        curr2 = dummy2
        node = head

        while node: 
            saved = node.next
            if node.val < x:
                curr.next = node
                curr = curr.next
            else:
                curr2.next = node
                curr2 = curr2.next
            node = saved
        curr2.next = None
        print(curr)
        print(dummy)
        print(dummy2)
        curr.next = dummy2.next
        return dummy.next
        
        