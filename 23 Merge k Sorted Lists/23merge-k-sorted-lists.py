# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        def merge(node1, node2):
            dummy = curr = ListNode(0)
            while node1 and node2:
                if node1.val < node2.val:
                    curr.next = node1
                    node1 = node1.next
                else:
                    curr.next = node2
                    node2 = node2.next
                curr = curr.next

            if node1:
                curr.next = node1
            
            if node2:
                curr.next = node2
            
            return dummy.next

        
        while len(lists) != 1:
            list1 = []
            for i in range(0, len(lists), 2):
                list_first = lists[i]
                list_second = lists[i + 1] if i + 1 < len(lists) else None
                list1.append(merge(list_first, list_second))
            lists = list1
            print(len(lists))
        
        return lists[0]