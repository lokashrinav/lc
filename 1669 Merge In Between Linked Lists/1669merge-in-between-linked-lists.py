# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        list2Head = list2
        prev = None
        while list2Head:
            prev = list2Head
            list2Head = list2Head.next
        list2Tail = prev
        
        node = list1
        count = 0
        prev = None
        while node:
            saved = node.next
            if count == a:
                prev.next = list2
            if count == b:
                list2Tail.next = saved
            prev = node
            node = saved
            count += 1
        return list1
        