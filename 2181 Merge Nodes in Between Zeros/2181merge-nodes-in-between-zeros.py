# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        node = head
        sum1 = -1
        curr = dummy
        while node:
            if node.val == 0 and sum1 == -1:
                sum1 = 0
                node = node.next
                continue
            elif node.val == 0:
                curr.next = ListNode(sum1)
                curr = curr.next
                sum1 = 0
            else:
                sum1 += node.val
            node = node.next

        return dummy.next
    