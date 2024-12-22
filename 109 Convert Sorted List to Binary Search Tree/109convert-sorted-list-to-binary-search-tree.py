# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def idk(head):
            if not head:
                return None
            if head and not head.next:
                return TreeNode(head.val)

            turtle, hare = head, head
            prev = None

            while hare and hare.next:
                hare = hare.next.next
                prev = turtle
                turtle = turtle.next

            saved = turtle.next
            turtle.next = None

            if prev:
                prev.next = None 
            first = head
            second = saved

            lis1 = idk(first)
            lis2 = idk(saved)

            newNode = TreeNode(turtle.val)
            newNode.left = lis1
            newNode.right = lis2
            return newNode

        return idk(head)

        