# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        node = head
        maxDistance = -1
        minDistance = -1
        startInd = None
        curr = 0
        prev = None
        while node and node.next and node.next.next:
            if node.next.val > node.val and node.next.val > node.next.next.val:
                if startInd is None:
                    startInd = curr
                else:
                    if minDistance == -1:
                        minDistance = float('inf')
                    print(curr - startInd)
                    maxDistance = max(curr - startInd, maxDistance)
                    minDistance = min(curr - prev, minDistance)
                prev = curr
                #print('2', curr, startInd, maxDistance)
            elif node.next.val < node.val and node.next.val < node.next.next.val:
                if prev is None:
                    startInd = curr
                else:
                    if minDistance == -1:
                        minDistance = float('inf')
                    minDistance = min(curr - prev, minDistance)
                    maxDistance = max(curr - startInd, maxDistance)
                prev = curr
                #print('1', curr, startInd, maxDistance)
            curr += 1
            node = node.next

        return [minDistance, maxDistance]

            

        