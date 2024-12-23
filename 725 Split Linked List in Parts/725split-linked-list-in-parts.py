# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        node = head
        count = 0
        while node:
            count += 1
            node = node.next
        
        rem = count % k
        div = count // k

        lis = []

        total = 1
        node = head

        curr = head
        
        for i in range(k):
            lis.append(curr)
            for p in range(div - 1 + (1 if rem else 0)):
                curr = curr.next
            
            if rem:
                rem -= 1

            if curr:
                saved = curr.next
                curr.next = None
                curr = saved

        return lis


        