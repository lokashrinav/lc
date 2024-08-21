# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count, node = 0, head
        prev = None
        head2 = head
        total = 0

        if k == 1:
            return head

        while head2:
            total += 1
            head2 = head2.next
        total = (total // k) * k
        next_node = None

        while True:
            if count == total: # Breaking Condition. Don't worry about it for now
                break
            if count < k: # Grabs head of linked list
                head2 = node
            if count == 0:
                saved_node = node
            elif next_node and (count + 1) % k == 0:
                next_node.next = node
                saved_node.next = node.next
                next_node = saved_node
                saved_node = node.next
            elif (count + 1) % k == 0:
                saved_node.next = node.next
                next_node = saved_node
                saved_node = node.next
            saved = node.next # Reversed first segement of linked list
            if count % k != 0:
                node.next = prev
            prev = node
            node = saved
            count += 1
        return head2
            