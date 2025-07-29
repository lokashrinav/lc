# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        def merge(list1, list2):
            head = node = ListNode()
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next
            
            if list1:
                node.next = list1
            if list2:
                node.next = list2
                
            return head.next
        
        while len(lists) > 1:
            curr = []
            for i in range(0, len(lists), 2):
                if i + 1 != len(lists):
                    curr.append(merge(lists[i], lists[i + 1]))
                else:
                    curr.append(lists[i])
            lists = curr
        
        return lists[0]
                
                

        