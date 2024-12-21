# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        value = []
        stack = []
        node = head

        while node:
            value.append(node.val)
            node = node.next
            
        ans = [0] * len(value)

        for i in range(len(value)):
            while stack and stack[-1][1] < value[i]:
                ind, val = stack.pop()
                ans[ind] = value[i]
            stack.append((i, value[i]))
        
        return ans
        

        



        