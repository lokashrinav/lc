# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        head2 = list2 = slow.next
        slow.next = None
        prev_val = None

        while head2:
            saved = head2.next
            head2.next = prev_val
            prev_val = head2
            head2 = saved

        list2 = prev_val
        list1 = head
        
        while list2:
            tmp1, tmp2 = list1.next, list2.next
            list1.next = list2
            list2.next = tmp1
            list1 = tmp1
            list2 = tmp2
        return head
        