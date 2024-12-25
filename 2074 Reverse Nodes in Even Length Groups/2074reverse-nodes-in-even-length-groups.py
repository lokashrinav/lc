# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 2
        node = head
        prev = node # Node(5)
        node = node.next # Node(2)

        while node:
            tempCount = count # 2
            saved2 = node
            while node and tempCount:
                node = node.next
                tempCount -= 1
            tempCount = count - tempCount   
            node = saved2           
            start = min(tempCount, count)
            if tempCount % 2 == 0:
                first = None # None
                while node and tempCount:  # Node(2) | Node(6)
                    saved = node.next # saved = Node(6) | saved = Node(3)
                    if tempCount != start: # 2 != 2 | 1 != 2
                        node.next = prev2 # Node(6) -> Node(2)
                    else:
                        first = node # first = Node(2)
                    prev2 = node # prev2 = Node(2) | prev2 = Node(6)
                    node = saved # node = Node(6) | node = Node(3)
                    tempCount -= 1 # temp = 1 | temp = 0

                prev.next = prev2 # Node(5) -> Node(6)
                prev = first # prev = Node(2)
                first.next = saved # Node(2) -> Node(3)
            else:
                prev2 = None
                while tempCount and node:
                    tempCount -= 1
                    prev2 = node
                    node = node.next
                prev = prev2

            count += 1

        return head
        